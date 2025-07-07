local M = {}

M.commands = function()
    vim.api.nvim_create_user_command("IsWorking", function()
        print("Yep!")
        print("Command executed successfully")
    end, {})
    vim.api.nvim_create_user_command("SuggestImports", function(opts)
        local args = opts.fargs
        local script_path = vim.fn.stdpath("config") .. "/lua/LazyDevHelper/python/pip_install.py"

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

    local commands = vim.api.nvim_get_commands({ scope = 'all' })
    local found = false
    for _, cmd in ipairs(commands) do
        if cmd.name == 'SuggestImports' then
            found = true
            break
        end
    end
    if not found then
        vim.notify('Error: SuggestImports command not registered', vim.log.levels.ERROR)
    end
end

M.commands()
return M
