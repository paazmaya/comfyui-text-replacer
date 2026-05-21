# ComfyUI node to replace words in prompts



## How it works

1.  **Persistence:**
    *   When you load a `workflow.json`, ComfyUI loads the rules saved inside that JSON.
    *   When you add a **new** node, it reads `default_rules.txt`.
    *   If you update `default_rules.txt` later, your old workflows remain exactly as they were (because the rules are saved in the workflow file), satisfying your requirement.

2.  **Validation:**
    *   When you type in the "Rules" box, the JavaScript `validateRules` function checks every line.
    *   If you type `badword` (no colon) and hit Enter, the box background turns **Red**.
    *   If you fix it to `badword:goodword`, the background turns back to normal.

3.  **Installation:**
    *   Just put the folder in `custom_nodes`.
    *   Restart ComfyUI (ComfyUI automatically finds `.js` files inside subfolders of `custom_nodes`).
  

## The Default Rules File

The `default_rules.txt` acts as the default source of word replacement rules for new nodes.

```text
# These are the default replacement rules
cat: dog
blue: red
happy: ecstatic
old: new
```

## License

MIT
