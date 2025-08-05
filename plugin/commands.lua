local M = {}

M.commands = function()
    vim.api.nvim_create_user_command("IsWorking", function()
        print("Yep!")
        print("Command executed successfully")
    end, {})

    vim.api.nvim_create_user_command("HellPip", function()
        print("Need help? Thats for u: ")
        print("Commands: \n:IsWorking - for check plugin status\n")
        print(":SuggestImports {lib_names (can be multiply)} - well.. main functional, maybe")
    end, {})

    vim.api.nvim_create_user_command("SuggestImports", function(opts)
        local args = opts.fargs
        local lang = vim.api.nvim_buf_get_option(0, "filetype")
        print("Detected filetype: " .. lang)

        local config_path = vim.fn.stdpath("config") .. '/lua/LazyDeveloperHelper/python/'
<<<<<<< HEAD
        local installers = {
            python = "pip_install.py",
            lua = "luarocks_install.py",
            rust = "cargo_install.py",
            javascript = "npm_install.py"
        }
        local script_name = installers[lang]
        if not script_name then
            print("No installer configured for filetype: " .. lang)
            return
        end

        local script_path = config_path .. script_name

        local function execute_command(script_path, lib)
            local cmd = string.format('python3 "%s" "%s"', script_path, lib)
            local output = vim.fn.system(cmd)
            print(output)
        end

        for _, lib in ipairs(args) do
            execute_command(script_path, lib)
        end
    end, nargs = '+'
=======

        -- table with format "lang name = installer file"
        local installers = {
            python = "pip_install.py",
            lua = "luarocks_install.py",
            rust = "cargo_install.py",
            javascript = "npm_install.py",
        }

        local script_name = installers[lang]
        if not script_name then
            print("No installer configured for filetype: " .. lang)
            return
        end

        local script_path = config_path .. script_name

        local function execute_command(script_path, lib)
            local cmd = string.format('python3 "%s" "%s"', script_path, lib)
            local output = vim.fn.system(cmd)
            return output
        end

        for _, lib in ipairs(args) do
            print("📦 Installing: " .. lib)
            local result = execute_command(script_path, lib)
            if result then
                print(result)
            else
                print("❌ Error executing command for " .. lib)
            end
        end
    end, { nargs = '+' })
>>>>>>> 8824c84 ([CHANGED FILE/DIR: plugin/commands.lua] Optimized logic with starting installers-files)
end
    
return M

