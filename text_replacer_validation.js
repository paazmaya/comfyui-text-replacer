import { app } from "../scripts/app.js";

// Register the extension
app.registerExtension({
    name: "WordReplacer.Validation",

    // This runs when a node is created
    nodeCreated(node) {
        // Check if this node is our WordReplacer
        if (node.comfyClass === "WordReplacer") {
            
            // Find the 'rules' widget
            const rulesWidget = node.widgets.find(w => w.name === "rules");

            if (rulesWidget) {
                // Function to validate the input
                const validateRules = (value) => {
                    const lines = value.split('\n');
                    let isValid = true;

                    for (let line of lines) {
                        // Remove whitespace
                        const trimmed = line.trim();
                        // Skip empty lines or comments
                        if (trimmed === "" || trimmed.startsWith("#")) {
                            continue;
                        }
                        // Check if it contains a colon
                        if (!trimmed.includes(":")) {
                            isValid = false;
                            break;
                        }
                    }

                    // Visual feedback: Change background color
                    if (rulesWidget.inputEl) {
                        if (!isValid) {
                            rulesWidget.inputEl.style.backgroundColor = "#ffcccc"; // Light Red
                            rulesWidget.inputEl.title = "Invalid Format: Every line must contain a colon (find:replace)";
                        } else {
                            rulesWidget.inputEl.style.backgroundColor = ""; // Reset to default
                            rulesWidget.inputEl.title = "";
                        }
                    }
                };

                // 1. Validate immediately when the node is created (to catch initial file load errors)
                validateRules(rulesWidget.value);

                // 2. Add a callback that triggers every time the user types
                // We use a slight timeout to not validate while the user is currently typing the colon
                const originalCallback = rulesWidget.callback;
                rulesWidget.callback = function(value) {
                    validateRules(value);
                    if (originalCallback) {
                        return originalCallback.apply(this, arguments);
                    }
                };
            }
        }
    }
});
