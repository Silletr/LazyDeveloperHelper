local M = {}

function M.register()
    vim.api.nvim_create_user_command("LazyDevInstall", function(opts)
        local fargs = vim.deepcopy(opts.fargs)
        local quiet = false
        local packages = {}

        -- Parse arguments in reverse to handle --quiet correctly
        for i = #fargs, 1, -1 do
            local arg = fargs[i]
            if arg == "--quiet" or arg == "-q" then
                quiet = true
                table.remove(fargs, i)
            else
                table.insert(packages, arg)
            end
        end

        if #packages == 0 then
            vim.notify("❌ Specify at least one package", vim.log.levels.ERROR)
            return
        end

        local lang = vim.api.nvim_buf_get_option(0, "filetype")
        vim.notify("Detected filetype: " .. lang, vim.log.levels.INFO)

        local config_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/"
        local installers = {
            python = "pip_install.py",
            lua = "luarocks_install.py",
            rust = "cargo_install.py",
            javascript = "npm_install.py",
            ruby = "ruby_gem_install.py",
            c = "c_installers/conan_install.py",
            cpp = "c_installers/nuget_install.py",
            kotlin = "java_installer/gradle_install.py",
        }
        local script_name = installers[lang]

        if not script_name then
            vim.notify("❌ No installer configured for filetype: " .. lang, vim.log.levels.WARN)
            return
        end

        local python_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python"
        local factory_path = python_path .. "/python_installers/factory.py"
        local cmd = { "python3", factory_path, lang, script_name, unpack(packages) }
        if quiet then
            table.insert(cmd, "--quiet")
        end

        local result = vim.system(cmd, { text = true })

        if result.code == 0 then
            if not quiet then
                vim.notify("✅ Installed " .. table.concat(packages, ", ") .. " (" .. lang .. ")", vim.log.levels.INFO)
            end
        else
            vim.notify(
                "❌ Failed to install " .. table.concat(packages, ", ") .. " (" .. lang .. ")",
                vim.log.levels.ERROR
            )
            if result.stderr and result.stderr ~= "" then
                vim.notify(result.stderr, vim.log.levels.ERROR)
            end
        end
    end, { nargs = "*" })
end

return M
