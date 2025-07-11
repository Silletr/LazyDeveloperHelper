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
    
        -- Define script paths relative to config directory
        local python_script = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/pip_install.py"
        local lua_script = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/luarocks_install.py"

        -- Function to safely execute external commands
        local function execute_command(script_path, lib)
            local cmd = string.format(
                'python3 -c "import subprocess; print(subprocess.run([\'%s\', \'%s\'], capture_output=True, text=True).stdout)"',
                script_path, lib
            )
            return vim.fn.system(cmd)
        end

        -- Process each library argument
        for _, lib in ipairs(args) do
            local result
        
            -- Determine which installer to use based on filetype
            if lang == "python" then
                print("🐍 Installing Python package: " .. lib)
                result = execute_command(python_script, lib)
            
            elseif lang == "lua" then
                print("💎 Installing Lua package: " .. lib)
                result = execute_command(lua_script, lib)
            
            else
                print(string.format("❌ Unsupported filetype '%s'", lang))
                print("Supported filetypes: python, lua")
            goto continue
            end

            -- Handle command output
            print("📦 Result for: " .. lib)
            if result then
                print(result)
            else
                print("❌ Error executing command")
            end
        ::continue::
        end
    end, { nargs = "+" })    
    -- vim.notify('Error: Command registration failed', vim.log.levels.ERROR)
end

return M
