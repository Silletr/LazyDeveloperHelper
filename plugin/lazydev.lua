vim.api.nvim_create_user_command("SuggestImports", function(opts)
        local args = opts.fargs
        local script_path = vim.fn.stdpath("config") .. "/lua/LazyDevHelper/python/pip_install.py"

        for _, lib in ipairs(args) do
            local result = vim.system({ "python3", script_path, lib }, { text = true }):wait()
            local output = vim.fn.system(result)
            print("📦 Result for: " .. lib)
            print(output)
            if result.code == 0 then
                print(result.stdout)
            else
                print("❌ Error:")
                print(result.stderr)
            end
        end
end, { nargs = "+" })


