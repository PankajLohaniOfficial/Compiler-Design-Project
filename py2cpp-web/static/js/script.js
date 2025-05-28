document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const isDark = localStorage.getItem("theme") === "dark";
    if (isDark) document.body.classList.add("dark-mode");

    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
    });

    CodeMirror.fromTextArea(document.getElementById("code"), {
        lineNumbers: true,
        mode: "python",
        theme: isDark ? "dracula" : "default"
    });

    const output = document.getElementById("output");
    if (output) {
        CodeMirror.fromTextArea(output, {
            lineNumbers: true,
            mode: "text/x-c++src",
            readOnly: true,
            theme: isDark ? "dracula" : "default"
        });
    }
});
