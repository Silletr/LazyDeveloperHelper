local M = {}

function M.register()
  vim.api.nvim_create_user_command("IsWorking", function()
    print("Yep!")
    print("Command executed successfully")
  end, {})

  vim.api.nvim_create_user_command("HellPip", function()
    print("Need help? Thats for u: ")
    print("Commands: \n:IsWorking - for check plugin status\n")
    print(":LazyDevInstall (-r or -silent (or both) {lib_names (can be multiply)} - \nwell.. main functional, maybe")
  end, {})

  vim.api.nvim_create_user_command("LazyDevHelp", function()
    print("More detailed about flags in command -\n")
    print("-r is - Requirements, like you saying 'install all requirements")
    print("from standart requirements file (Python - requirements.txt, Cargo - Cargo.toml block [Dependencies]'")
  end, {})
end

return M
