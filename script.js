function showForm(formid){
    document.querySelectorAll(".form-container").forEach(form => form.classList.remove("active"));
    document.getElementById(formid).classList.add("active");
}