document.addEventListener("DOMContentLoaded", function () {
  // Fake in memory filesystem
  var fs = {
  };

  var path = [];
  var cwd = fs;

  function restore_cwd(fs, path) {
    path = path.slice();
    while (path.length) {
      var dir_name = path.shift();
      if (!is_dir(fs[dir_name])) {
        throw new Error(
          "Internal Error Invalid directory " +
            $.terminal.escape_brackets(dir_name)
        );
      }
      fs = fs[dir_name];
    }
    return fs;
  }
  function clean_path(p) {
    if (p.endsWith("/")) {
      p = p.slice(0, -1);
    }
    if (p.startsWith("/")) {
      p = p.slice(1);
    }
    return p;
  }
  function is_dir(obj) {
    return typeof obj === "object";
  }
  function is_file(obj) {
    return typeof obj === "string";
  }
  function is_path(p) {
    p = clean_path(p);
    path_list = p.split("/");
    tfp = fs;
    for (const k of path_list) {
      if (Object.keys(tfp).includes(k)) {
        tfp = tfp[k];
      } else {
        return null;
      }
    }
    if (is_dir(tfp)) {
      return "dir";
    } else if (is_file(tfp)) {
      return "file";
    }
  }
  function move_to(p) {
    if (is_path(p) == "dir") {
      p = clean_path(p);
      path_list = p.split("/");
      for (const k of path_list) {
        if (Object.keys(cwd).includes(k)) {
          cwd = cwd[k];
        } else {
          return;
        }
      }
    }
  }
  function grab_file(p) {
    if (is_path(p) == "file") {
      p = clean_path(p);
      path_list = p.split("/");
      tfp = fs;
      for (const k of path_list) {
        if (Object.keys(tfp).includes(k)) {
          tfp = tfp[k];
        } else {
          return null;
        }
      }
      return tfp;
    }
  }
  function pop_fs() {
    var settings = {
      url: `${window.location.protocol}//${window.location.host}/resumeapi/`,
      method: "GET",
      timeout: 0,
    };
    console.log(window.location.host);
    $.ajax(settings).done(function (r) {
      for (const model in r) {
        var settings = {
          url: `${window.location.protocol}//${window.location.host}/resumeapi/${model}/`,
          method: "GET",
          timeout: 0,
        };
        fs[model] = {};
        $.ajax(settings).done(function (response) {
          for (const i in response) {
            //0, 1, 2, etc.
            for (const j in response[i]) {
              //id, company, position, etc.
              if (j !== "id") {
                response[i][j + ".txt"] = response[i][j];
              }
              delete response[i][j];
            }
            var name = response[i][Object.keys(response[i])[0]].replaceAll(
              " ",
              "_"
            );
            fs[model][name] = response[i];
          }
        });
      }
    });
  }

  var descriptions = {
    cd: {
      name: "cd",
      description: "Changes directory.",
      usage: "cd <dir path>",
      example: "cd projects/",
    },

    pwd: {
      name: "pwd",
      description: "Prints the current working directory.",
      usage: "pwd",
      example: "pwd",
    },

    tree: {
      name: "tree",
      description: "Lists all files and directories in filesystem",
      usage: "tree",
      example: "tree",
    },
    ls: {
      name: "ls",
      description: "Lists all files and directories relative to CWD.",
      usage: "ls <optional arg '-a'>",
      example: "ls <or> ls -a",
    },
    cat: {
      name: "cat",
      description: "Concatenates a file.",
      usage: "cat <file path>",
      example: "cat baz.txt",
    },
    vim: {
      name: "vim",
      description: "Creates a text file at the current working directory.",
      usage: "vim <file name> <text for file>",
      example: "vim testfile.txt Wow I love test files, these are great!",
    },
    rm: {
      name: "rm",
      description: "Deletes a file at the current working directory.",
      usage: "rm <file name>",
      example: "rm testfile.txt",
    },
    mkdir: {
      name: "mkdir",
      description: "Creates a directory at the current working directory.",
      usage: "mkdir <dir name>",
      example: "mkdir testdir",
    },
    rmdir: {
      name: "rmdir",
      description:
        "Deletes a directory (recursively) at the current working directory.",
      usage: "rmdir <dir name>",
      example: "rmdir testdir",
    },
    ping: {
      name: "ping",
      description: "Sends a fake ping, recieves a pong.",
      usage: "ping",
      example: "pong",
    },
    echo: {
      name: "echo",
      description: "Echos text back to the user.",
      usage: "echo <text>",
      example: "echo foo bar",
    },
    help: {
      name: "help",
      description:
        "Lists all available commands, including usage and examples.",
      usage: "help",
      example: "help",
    },
    man: {
      name: "man",
      description:
        "Lists the name, description, usage, and examples for the specified command.",
      usage: "man <command>",
      example: "man cat",
    },
  };

  var commands = {
    pwd: function () {
      full_path = `/home/${document.getElementById("username").value}`;
      if (path != false) {
        full_path += "/" + path.join("/");
      }
      term.echo(full_path);
    },

    test: function (...args) {
      if (args.length > 2 || args.length == 0) {
        term.echo("Incorrect number of arguments");
        return;
      }

      const p = args[0];

      if (args.includes("-f") && is_path(p) == "file") {
        term.echo("This is a valid file path!");
      } else if (args.includes("-d") && is_path(p) == "dir") {
        term.echo("This is a valid folder path!");
      } else if (is_path(p) && args.length == 1) {
        term.echo("This is a valid path!");
      } else {
        term.echo("This isn't a valid path or path type!");
      }
    },

    cd: function (dir) {
      this.pause();
      if (dir === "/" || !dir || dir === "~") {
        path = [];
        cwd = restore_cwd(fs, path);
      } else if (dir === "..") {
        if (path.length) {
          path.pop(); // remove from end
          cwd = restore_cwd(fs, path);
        }
      } else if (dir.match(/\//) && is_path(dir) == "dir") {
        var p = dir.replace(/\/$/, "").split("/").filter(Boolean);
        console.log("P: " + p);
        if (dir[0] !== "/") {
          p = path.concat(p);
        }
        cwd = restore_cwd(fs, p);

        path = p;
      } else if (
        !is_path(path.join("/") + "/" + dir) ||
        is_path(path.join("/") + "/" + dir) == "file"
      ) {
        if (is_path(path.join("/") + "/" + dir) == "file") {
          this.error(
            "bash: cd: " + $.terminal.escape_brackets(dir) + ": Not a directory"
          );
        } else {
          console.log(path.join("/") + dir);
          this.error(
            "bash: cd: " +
              $.terminal.escape_brackets(dir) +
              ": No such file or directory"
          );
        }
      } else {
        dir = clean_path(dir);
        cwd = cwd[dir];
        path.push(dir);
      }

      this.resume();
    },

    tree: function (arg) {
      if (!is_dir(cwd)) {
        throw new Error("Internal Error Invalid directory");
      }

      function filetree(d, tabs) {
        return Object.keys(d).map(function (key) {
          var structure = "";
          for (var x = 0; x < tabs; x++) {
            if (x == tabs - 1) {
              structure += "  |_";
            } else {
              structure += "\t";
            }
          }
          if (is_dir(d[key])) {
            var fcwd = d[key];

            return structure + key + "/\n" + filetree(fcwd, tabs + 1);
          } else if (arg == "-a" && is_file(d[key])) {
            return structure + key + "\n\t\t >> " + d[key] + "\n";
          }

          return structure + key + "\n";
        });
      }

      var dir = filetree(fs, 0).join("");

      var parsed_dir = "";
      for (var x = 0; x < dir.length; x++) {
        if (x != 0 && dir[x - 1] === "\n" && dir[x] === ",") {
          parsed_dir += " ";
        } else {
          parsed_dir += dir[x];
        }
      }
      this.echo(parsed_dir);
    },
    ls: function (txt) {
      if (txt === "-a") {
        function filetree(d, tabs) {
          return Object.keys(d).map(function (key) {
            var structure = "";
            for (var x = 0; x < tabs; x++) {
              if (x == tabs - 1) {
                structure += "|_";
              } else {
                structure += "\t";
              }
            }
            if (is_dir(d[key])) {
              var fcwd = d[key];

              return structure + key + "/\n" + filetree(fcwd, tabs + 1);
            }
            return structure + key + "\n";
          });
        }

        var dir = filetree(cwd, 0);

        this.echo(dir.join("").replaceAll(",", ""));
      } else {
        if (!is_dir(cwd)) {
          throw new Error("Internal Error Invalid directory");
        }

        var dir = Object.keys(cwd).map(function (key) {
          if (is_dir(cwd[key])) {
            return key + "/";
          }
          return key;
        });

        this.echo(dir.join("\n"));
      }
    },

    mkdir: function (n) {
      cwd[n] = {};
    },
    rmdir: function (n) {
      if (is_path(path.join("/") + "/" + n) != "dir") {
        term.echo("rmdir: failed to remove '" + n + "' : No such directory");
      } else {
        delete cwd[n];
      }
    },
    vim: function (...args) {
      if (args.length < 2) {
        term.echo("vim: incorrect number of arguments, try 'man vim'");
      } else {
        cwd[args[0]] = args.slice(1).join(" ");
      }
    },
    rm: function (n) {
      if (is_path(path.join("/") + "/" + n) != "file") {
        term.echo("rm: failed to remove '" + n + "' : No such file");
      } else {
        delete cwd[n];
      }
    },
    cat: function (file) {
      if (is_path(path.join("/") + "/" + file) == "file") {
        this.echo(grab_file(path.join("/") + "/" + file));
      } else if (is_file(cwd[file])) {
        this.echo(cwd[file]);
      } else if (is_path(file) == "dir") {
        this.error(
          "cat: " +
            $.terminal.escape_brackets(file) +
            ": Can not concatenate a directory"
        );
      } else {
        this.error(
          "cat: " + $.terminal.escape_brackets(file) + ": File not found"
        );
      }
    },
    ping: function () {
      this.echo("pong");
    },
    echo: function (...txt) {
      var command = this.get_command();
      var cmd = $.terminal.parse_command(command);
      this.echo(cmd.rest);
    },
    help: function () {
      this.echo("Available commands:\n--");
      for (const key of Object.keys(descriptions)) {
        var cmd = descriptions[key];
        this.echo(cmd["name"]);
        this.echo("description: " + cmd["description"]);
        this.echo("usage: " + cmd["usage"]);
        this.echo("--");
      }
    },
    man: function (arg) {
      if (arg && arg in descriptions === false) {
        this.echo("No manual entry for " + arg);
      } else if (arg in descriptions) {
        var cmd = descriptions[arg];
        this.echo("name: " + cmd["name"]);
        this.echo("description: " + cmd["description"]);
        this.echo("usage: " + cmd["usage"]);
        this.echo("example: " + cmd["example"]);
      } else {
        this.echo("What manual page do you want?\nFor example, try 'man man'.");
      }
    },
  };

  function completion(string, callback) {
    var command = this.get_command();
    var cmd = $.terminal.parse_command(command);
    function dirs(cwd) {
      return Object.keys(cwd)
        .filter(function (key) {
          if (cmd.name === "cd") {
            return is_dir(cwd[key]);
          } else {
            return is_file(cwd[key]) || is_dir(cwd[key]);
          }
        })
        .map(function (dir) {
          if (is_path(dir) == "dir" || is_dir(cwd[dir])) return dir + "/";
          else return dir;
        });
    }
    if (cmd.name === "ls") {
      callback([]);
    } else if (["cd", "test", "cat"].includes(cmd.name)) {
      var p = string.split("/").filter(Boolean);

      if (p.length === 1) {
        if (string[0] === "/") {
          callback(dirs(fs));
        } else {
          callback(dirs(cwd));
        }
      } else {
        if (!string) {
          return;
        }
        if (string[0] !== "/") {
          p = path.concat(p);
        }
        if (string[string.length - 1] !== "/") {
          p.pop();
        }
        var prefix = string.replace(/\/[^/]*$/, "");
        callback(
          dirs(restore_cwd(fs, p)).map(function (dir) {
            return prefix + "/" + dir;
          })
        );
      }
    } else if (cmd.name === "cat") {
      var files = Object.keys(cwd).filter(function (key) {
        return is_file(cwd[key]);
      });
      callback(files);
    } else {
      callback(Object.keys(commands));
    }
  }

  function prompt(user) {
    return function (callback) {
      var prompt;

      prompt = `${user}@heyerapp:~`;
      if (path != false) {
        prompt += "/";
      }
      prompt += path.join("/") + "$ ";
      $(".title").html(prompt);
      callback(prompt);
    };
  }

  var scanlines = $(".scanlines");
  var tv = $(".tv");
  function exit() {
    $(".tv").addClass("collapse");
    term.disable();
  }

  var __EVAL = (s) => eval(`void (__EVAL = ${__EVAL}); ${s}`);

  //TERMINAL INIT
  var term = $("#terminal").terminal(commands, {
    name: "heyerappterm",
    onResize: set_size,
    exit: false,
    completion: completion,
    checkArity: false,
    enabled: $("body").attr("onload") === undefined,
    onInit: function () {
      //WHEN TERMINAL IS FIRST INITIALIZED
      pop_fs();
      set_size();

      if (document.getElementById("useragent")) {
        let detection =
          "MOBILE DEVICE DETECTED\nHeyerApp's Terminal is not yet intended for mobile devices.\n";

        this.echo(detection);
        this.disable();
      } else {
        this.echo("Type 'help' or double-tab for list of commands.\nFor résumé via filesystem, type 'tree -a', else go here <https://heyer.app/resume>.");
      }
    },

    prompt: prompt(document.getElementById("username").value),
  });

  function set_size() {
    // for window height of 170 it should be 2s
    var height = $(window).height();
    var width = $(window).width();
    var time = (height * 2) / 170;
    scanlines[0].style.setProperty("--time", time);
    tv[0].style.setProperty("--width", width);
    tv[0].style.setProperty("--height", height);
  }
});
