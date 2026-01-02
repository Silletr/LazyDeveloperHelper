local M = {}

local function detect_manager(lang)
    local map = {
        python = "pip",
        lua = "luarocks",
        rust = "cargo",
        javascript = "npm",
        typescript = "npm",
        ruby = "ruby-gem",
        c = "conan",
        cpp = "conan",
        kotlin = "gradle",
        java = "gradle",
    }
    return map[lang] or "pip"
end

local function install_packages(packages, manager, quiet)
    local python_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python"
    local factory_path = python_path .. "/python_installers/factory.py"

    for _, pkg in ipairs(packages) do
        local cmd = { "python3", factory_path, manager, pkg }
        if quiet then
            table.insert(cmd, "--quiet")
        end

        local result = vim.system(cmd, { text = true })

        if result.code == 0 then
            if not quiet then
                vim.notify("✅ Installed " .. pkg .. " (" .. manager .. ")", vim.log.levels.INFO)
            end
        else
            vim.notify("❌ Failed to install " .. pkg .. " (" .. manager .. ")", vim.log.levels.ERROR)
            if result.stderr and result.stderr ~= "" then
                vim.notify(result.stderr, vim.log.levels.ERROR)
            end
        end
    end
end

function M.register()
    vim.api.nvim_create_user_command("LazyDevInstall", function(opts)
        local fargs = vim.deepcopy(opts.fargs)
        local manager = nil
        local quiet = false
        local packages = {}

        -- Parse arguments in reverse to handle --manager value correctly
        for i = #fargs, 1, -1 do
            local arg = fargs[i]
            if arg == "--quiet" or arg == "-q" then
                quiet = true
                table.remove(fargs, i)
            elseif arg:match("^%-%-manager=") then
                local captured = arg:match("^%-%-manager=(.*)")
                if captured then
                    manager = captured
                    vim.notify("Manager: " .. manager)
                    table.remove(fargs, i)
                else
                    vim.notify("❌ Invalid --manager= format", vim.log.levels.ERROR)
                end
            elseif arg == "--manager" then
                if i + 1 <= #fargs then
                    manager = fargs[i + 1]
                    table.remove(fargs, i + 1)
                    table.remove(fargs, i)
                else
                    vim.notify("❌ --manager requires a value", vim.log.levels.ERROR)
                    return
                end
            else
                table.insert(packages, arg)
            end
        end

        if #packages == 0 then
            vim.notify("❌ Specify at least one package", vim.log.levels.ERROR)
            return
        end

        if not manager then
            -- Auto-detect by filetype - for convenience
            local lang = vim.api.nvim_buf_get_option(0, "filetype")
            manager = detect_manager(lang)
        end

        install_packages(packages, manager, quiet)
    end, { nargs = "*" })
end

return M
