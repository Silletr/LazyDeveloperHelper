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
        local script_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/pip_install.py"

        for _, lib in ipairs(args) do
            local cmd = string.format(
                'python3 -c "import subprocess; print(subprocess.run([\'%s\', \'%s\'], capture_output=True, text=True).stdout)"',
                script_path, lib
            )
            local result = vim.fn.system(cmd)

            print("📦 Result for: " .. lib)
            if result then
                print(result)
            else
                print("❌ Error executing command")
            end
        end
    end, { nargs = "+" })

    -- Check commands immediately after creation
    local commands = vim.api.nvim_get_commands({ scope = 'all' })
    for _, cmd in ipairs(commands) do
        -- Commands are prefixed with 'User '
        if string.match(cmd.name, '^User SuggestImports$') then
            vim.notify('Command registered successfully', vim.log.levels.INFO)
            return
        end
    end
    
    vim.notify('Error: Command registration failed', vim.log.levels.ERROR)
end

M.commands()
return M
