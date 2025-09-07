local M = {}

M.commands = function()
  -- Define supported filetypes and their corresponding installer scripts
  local installers = {
    python = "pip_install.py",
    lua = "luarocks_install.py",
    rust = "cargo_install.py",
    javascript = "npm_install.py",
  }

  -- Base path for installer scripts
  local config_path = vim.fn.stdpath("config") .. "/lua/LazyDeveloperHelper/python/"

  -- Command: Check plugin status
  vim.api.nvim_create_user_command("IsWorking", function()
    vim.notify("Yep! Command executed successfully", vim.log.levels.INFO)
  end, {})

  -- Command: Display help information
  vim.api.nvim_create_user_command("HellPip", function() 
      vim.notify("Need help? Thats for u: ")
      vim.notify("Commands: \n:IsWorking - for check plugin status\n")
      vim.notify(":SuggestImports {lib_names (can be multiply)} - well.. main functional, maybe")
  end, {})

  -- Command: Install libraries for the detected filetype
  vim.api.nvim_create_user_command("SuggestImports", function(opts)
    local args = opts.fargs
    if #args == 0 then
      vim.notify("No libraries specified for installation", vim.log.levels.WARN)
      return
    end

    local lang = vim.api.nvim_buf_get_option(0, "filetype")
    local script_name = installers[lang]
    if not script_name then
      vim.notify("No installer configured for filetype: " .. lang, vim.log.levels.WARN)
      return
    end

    local script_path = config_path .. script_name
    if vim.fn.filereadable(script_path) == 0 then
      vim.notify("Installer script not found: " .. script_path, vim.log.levels.ERROR)
      return
    end

    local function execute_async(lib)
      local stdout = vim.loop.new_pipe(false)
      local stderr = vim.loop.new_pipe(false)
      local output = {}
      local handle

      vim.notify("📦 Installing: " .. lib, vim.log.levels.INFO)

      handle = vim.loop.spawn("python3", {
        args = { script_path, lib },
        stdio = { nil, stdout, stderr },
      }, function(code)
        stdout:read_stop()
        stderr:read_stop()
        stdout:close()
        stderr:close()
        if handle then handle:close() end

        vim.schedule(function()
          if #output > 0 then
            vim.notify(table.concat(output), vim.log.levels.INFO)
          end
          if code == 0 then
            vim.notify("Successfully installed: " .. lib, vim.log.levels.INFO)
          else
            vim.notify("Failed to install: " .. lib .. " (code: " .. code .. ")", vim.log.levels.ERROR)
          end
        end)
      end)

      stdout:read_start(function(err, data)
        if err then
          vim.schedule(function()
            vim.notify("Error reading stdout: " .. err, vim.log.levels.ERROR)
          end)
          return
        end
        if data then
          table.insert(output, data)
        end
      end)

      stderr:read_start(function(err, data)
        if err then
          vim.schedule(function()
            vim.notify("Error reading stderr: " .. err, vim.log.levels.ERROR)
          end)
          return
        end
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
