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
        local scripts_path = {
            python_script = vim.fn.stdpath("config") .. 'lua/LazyDeveloperHelper/python/pip_install.py',
            lua_script = vim.fn.stdpath("config") .. 'lua/LazyDeveloperHelper/python/luarocks_install.py',
            rust_script = vim.fn.stdpath("config") .. 'lua/LazyDeveloperHelper/python/cargo_install.py',
            js_script = vim.fn.stdpath("config") .. 'lua/LazyDeveloperHelper/python/npm_install.py'}

        -- Function to safely execute external commands
        local function execute_command(script_path, lib)
            local cmd = string.format('python3 "%s" "%s"', script_path, lib)
            return vim.fn.system(cmd)
        end

        -- Process each library argument
        for _, lib in ipairs(args) do
            local result

            -- Determine which installer to use based on filetype
            if lang == "python" then
                print("🐍 Installing Python package: " .. lib)
                result = execute_command(scripts_path["python_script"], lib)

            elseif lang == "lua" then
                vim.notify("💎 Installing Lua package: " .. lib)
                result = execute_command(scripts_path["lua_script"], lib)
            elseif lang == "rust" then
                vim.notify("🦀 Installing Rust package: ".. lib)
                result = execute_comamnd(scripts_path["rust_script"], lib)
            elseif lang == "javascript" then
                vim.notify("☕ Installing JS package: ".. lib)
                result = execute_command(scripts_path["js_script"], lib)
            else
                print(string.format("❌ Unsupported filetype '%s'", lang))
                print("Supported filetypes: python, lua, rust, javasript")
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
