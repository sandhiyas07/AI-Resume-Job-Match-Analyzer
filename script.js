const form = document.getElementById("resumeForm");
const analyzeButton = document.getElementById("analyzeButton");
const loading = document.getElementById("loading");
const resultSection = document.getElementById("resultSection");
const resultContent = document.getElementById("resultContent");
const errorMessage = document.getElementById("errorMessage");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const resumeFile = document.getElementById("resume").files[0];
    const jobDescription = document.getElementById("job_description").value.trim();

    errorMessage.classList.add("hidden");
    resultSection.classList.add("hidden");

    if (!resumeFile) {
        showError("Please select a resume PDF.");
        return;
    }

    if (!resumeFile.name.toLowerCase().endsWith(".pdf")) {
        showError("Please upload a PDF file only.");
        return;
    }

    if (!jobDescription) {
        showError("Please enter the job description.");
        return;
    }

    const formData = new FormData();

    formData.append("resume", resumeFile);
    formData.append("job_description", jobDescription);

    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";

    loading.classList.remove("hidden");

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(
                data.message || "Something went wrong while analyzing the resume."
            );
        }

        resultContent.textContent = data.result;
        resultSection.classList.remove("hidden");

        resultSection.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {
        showError(error.message);
    } finally {
        loading.classList.add("hidden");

        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Resume";
    }
});


function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove("hidden");
}