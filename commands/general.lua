local M = {}

function M.register()
  vim.api.nvim_create_user_command("IsWorking", function()
    print("Yep!")
    print("Command executed successfully")
  end, {})

  vim.api.nvim_create_user_command("HellPip", function()
    print("Need help? Thats for u: ")
    print("Commands: \n:IsWorking - for check plugin status\n")
    print(":LazyDevInstall (if u wanna write -silent) {lib_names (can be multiply)} - \nwell.. main functional, maybe")
  end, {})
  vim.api.nvim_create_user_command("LazyDevTelemetry", function()
    -- WORK WILL BE STARTED SOON
    -- LINK TO GITHUB GIST - https://gist.github.com/Silletr/8f539cb32c31232d1c1f5129d34b6292
  end, {})
end
return M
