{
  description = "Python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        pythonEnv = pkgs.python3;
      in
      {
        devShell = pkgs.mkShell {
          packages = [
            pythonEnv
          ];
          shellHook = ''
            echo "Python environment activated"
            python --version
            exec zsh
          '';
        };
      });
}
