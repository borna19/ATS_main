async function submitForm() {
    const jd = document.getElementById("jd").value;
    const files = document.getElementById("files").files;

    if (!jd || files.length === 0) {
        alert("Please upload resumes and enter JD");
        return;
    }

    let formData = new FormData();
    formData.append("job_description", jd);

    for (let f of files) {
        formData.append("files", f);
    }

    const res = await fetch("http://localhost:8000/rank", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    localStorage.setItem("ranked", JSON.stringify(data.results));

    window.location.href = "result.html";
}
