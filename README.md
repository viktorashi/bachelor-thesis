# My bachelor thesis
My bachelor's LaTeX files, aslo hosted on [Papeeria](https://www.papeeria.com/join?token_id=bef97a1e-b804-4f2d-93a0-27f7bc0b9560&retry=3) and [Overleaf](https://www.overleaf.com/read/kqnmqfpwprzr#135c7d)

The app related to the project can be viewed [here](https://github.com/viktorashi/Open-CoNtRol)


pana acm am folosit latexmk cu optiunea de -f forced gen ca sa-mi mearga asta , deci da, sa se stie, comanda pe care o face extensie de latex-workshop e

```bash
    #in unde e main.tex
    cd .../..../bachelor-thesis

    #preferabil
    ls | grep main
    main.tex
```
```
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
"env": {}
```

Cand vrei sa formatezi, recomand sa iei [tex-fmt](https://github.com/WGUNDERWOOD/tex-fmt) si sa te folosesti de `tex-fmt.toml` care e acl in root (foloseste automat doar cand dai)

```bash
    tex-fmt file.tex
```

Dar daca nu-ti formateaza bine, dai un ca se foloseste de latexindent care e defaultu
```bash
    make
```

din root de unde e 
```bash
    ls | grep Makefile
    Makefile
```

sau daca vrei specific fix un anumit fisier:

```bash
make -b file.tex
```



asta in caz ca incercati sa dati compile singur ,ca sa stau sa tin track la fiecare versiune din .pdf in sine kinda defeats the purpose, asa nici macar nu poa sa faca vreun diff sau compresie din aia desteapa gitul ca el nu vede decat linii si ala e binar lol