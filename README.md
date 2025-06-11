# My bachelor thesis

My bachelor's LaTeX files, aslo hosted on [Papeeria](https://www.papeeria.com/join?token_id=bef97a1e-b804-4f2d-93a0-27f7bc0b9560&retry=3) and [Overleaf](https://www.overleaf.com/read/kqnmqfpwprzr#135c7d)

The app related to the project can be viewed [here](https://github.com/viktorashi/Open-CoNtRol)

#### Building, will default to `lualatex`:

```bash
    #in unde e main.tex
    cd bachelor-thesis
    #runs lualatex
    make
```

configu pe care-l am pt [latex Workshop pe vscode](https://github.com/James-Yu/latex-workshop) in `settings.json`:

```json
"command": "latexmk",
"args": [
    "-f",
    "-synctex=1",
    "-interaction=nonstopmode",
    "-file-line-error",
    "-pdf",
    "-outdir=%OUTDIR%",
    "%DOC%"
],
```

unde ar trb sa-ti pui

```json
"latex-workshop.latex.outDir": "build",
```

si unde `%DOC%` se pune singur sa fie `main.tex`

Cand vrei sa formatezi, recomand sa iei [tex-fmt](https://github.com/WGUNDERWOOD/tex-fmt) si sa te folosesti de `tex-fmt.toml` care e acl in root

si poti adica doar sa dai sa-ti dea singur format cu asta in setari la vscode daca folosesti [latex Workshop pe vscode](https://github.com/James-Yu/latex-workshop)

```json
"latex-workshop.formatting.tex-fmt.args": [
"--config",
"tex-fmt.toml"
],
```

sau poti direct cu latexindent care il are cam toata lumea

```bash
    make indent
```
