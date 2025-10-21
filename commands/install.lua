local M = {}

function M.register()
  vim.api.nvim_create_user_command("LazyDevInstall", function(opts)
    local args = opts.fargs
    local lang = vim.api.nvim_buf_get_option(0, "filetype")

    print("Detected filetype: " .. lang)

    local config_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/"
    local installers = {
      python = "pip_install.py",
      lua = "luarocks_install.py",
      rust = "cargo_install.py",
      javascript = "npm_install.py",
    }
    local script_name = installers[lang]
    if not script_name then
      vim.notify("❌ No installer configured for filetype: " .. lang, vim.log.levels.WARN)
      return
    end

    local script_path = config_path .. script_name

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

    for _, lib in ipairs(args) do
      execute_async(lib)
    end
  end, { nargs = "+" })
end

return M
