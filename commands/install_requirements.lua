local M = {}

function M.register()
  vim.api.nvim_create_user_command("LazyDevInstallRequirements", function()
    local lang = vim.api.nvim_buf_get_option(0, "filetype")
    local config_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/"
    local installers = {
      python = "requirements_installers/pip_req_install.py",
      rust = "requirements_installers/cargo_req_install.py",
    }

    local script_name = installers[lang]
    if not script_name then
      vim.notify("❌ No installer configured for filetype: " .. lang, vim.log.levels.WARN)
      return
    end

    local script_path = config_path .. script_name
    local libs = {}

    if lang == "python" then
      local req_file = vim.fn.getcwd() .. "/requirements.txt"
      if vim.fn.filereadable(req_file) == 0 then
        vim.notify("❌ requirements.txt not found!", vim.log.levels.WARN)
        return
      end
      for line in io.lines(req_file) do
        if line:match("%S") then
          table.insert(libs, line)
        end
      end
    elseif lang == "rust" then
      local cargo_file = vim.fn.getcwd() .. "/Cargo.toml"
      if vim.fn.filereadable(cargo_file) == 0 then
        vim.notify("❌ Cargo.toml not found!", vim.log.levels.WARN)
        return
      end
      for line in io.lines(cargo_file) do
        local dep = line:match("^%s*([%w_-]+)%s*=")
        if dep then table.insert(libs, dep) end
      end
    else
      vim.notify("❌ Requirements install not supported for: " .. lang, vim.log.levels.WARN)
      return
    end

    local function execute_async(lib)
      local stdout = vim.loop.new_pipe(false)
      local stderr = vim.loop.new_pipe(false)

      vim.notify("📦 Installing: " .. lib)

      local handle
      handle = vim.loop.spawn("python3", {
        args = { script_path, lib },
        stdio = { nil, stdout, stderr },
      }, function(code)
        stdout:read_stop()
        stderr:read_stop()
        stdout:close()
        stderr:close()
        handle:close()

        vim.schedule(function()
          if code == 0 then
            vim.notify("✅ Successfully installed " .. lib)
          else
            vim.notify("❌ Failed to install " .. lib .. " (code: " .. code .. ")", vim.log.levels.ERROR)
          end
        end)
      end)

      stdout:read_start(function(err, data)
        if data then
          vim.schedule(function()
            vim.notify(data, vim.log.levels.INFO)
          end)
        end
      end)

      stderr:read_start(function(err, data)
        if data then
          vim.schedule(function()
            vim.notify(data, vim.log.levels.ERROR)
          end)
        end
      end)
    end

    for _, lib in ipairs(libs) do
      execute_async(lib)
    end
  end, {})
end

return M
