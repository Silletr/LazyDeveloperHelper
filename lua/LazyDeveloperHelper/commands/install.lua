local M = {}

function M.register()
    vim.api.nvim_create_user_command("LazyDevInstall", function(opts)
        local fargs = vim.deepcopy(opts.fargs)
        local flag = false
        local lang = vim.api.nvim_buf_get_option(0, "filetype")

        for i = #fargs, 1, -1 do
            if fargs[i] == "--quiet" or fargs[i] == "-q" then
                flag = true
                table.remove(fargs, i)
                break
            end
        end
        local args = fargs
        if #args == 0 then
            vim.notify("❌ You must specify at least one library!", vim.log.levels.ERROR)
            return
        end

        vim.notify("Detected filetype: " .. lang, vim.log.levels.INFO)
        vim.notify("Active flags: " .. tostring(flag), vim.log.levels.DEBUG)

        local installers = {
            python = "pip_install.py",
            lua = "luarocks_install.py",
            rust = "cargo_install.py",
            javascript = "npm_install.py",
            ruby = "ruby_gem_install.py",
            c = "c_installers/conan_install.py",
            cpp = "c_installers/nuget_install.py",
            kotlin = "java_installer/gradle_install.py",
            go = "go_installer/go_installer.py",
        }
        local script_name = installers[lang]

        if not script_name then
            vim.notify("❌ No installer configured for filetype: " .. lang, vim.log.levels.WARN)
            return
        end

        local function get_plugin_python_path()
            local runtime_paths = vim.api.nvim_list_runtime_paths()
            for _, path in ipairs(runtime_paths) do
                if path:match("LazyDeveloperHelper") then
                    return path .. "/lua/LazyDeveloperHelper/python/"
                end
            end
            error("LazyDeveloperHelper not found in runtimepath!")
        end

        local python_dir = get_plugin_python_path()

        local script_path = python_dir .. script_name
        local function execute_async(lib)
            local stdout = vim.loop.new_pipe(false)
            local stderr = vim.loop.new_pipe(false)
            local current_file_dir = vim.fn.expand("%:p:h")

            vim.notify("📦 Installing: " .. lib .. (flag and " (with flag)" or ""))

            local spawn_args = { script_path, lib }
            if flag and lang == "python3" then
                table.insert(spawn_args, "-quiet")
            elseif flag and (lang == "lua" or lang == "javascript") then
                table.insert(spawn_args, "-q")
            end

            local handle
            handle = vim.loop.spawn("python3", {
                args = spawn_args,
                cwd = current_file_dir,
                stdio = { nil, stdout, stderr },
            }, function(code)
                stdout:read_stop()
                stderr:read_stop()
                stdout:close()
                stderr:close()
                handle:close()

                vim.schedule(function()
                    if code == 0 then
                        vim.notify("✅ Successfully installed " .. lib)
                    else
                        vim.notify("❌ Failed to install " .. lib .. " (code: " .. code .. ")", vim.log.levels.ERROR)
                    end
                end)
            end)

            stdout:read_start(function(err, data)
                if data then
                    vim.schedule(function()
                        vim.notify(data, vim.log.levels.INFO)
                    end)
                end
            end)

            stderr:read_start(function(err, data)
                if data then
                    vim.schedule(function()
                        vim.notify(data, vim.log.levels.ERROR)
                    end)
                end
            end)
        end

        for _, lib in ipairs(args) do
            execute_async(lib)
        end
    end, { nargs = "+" })
end

return M
