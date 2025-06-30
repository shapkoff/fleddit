const form = document.getElementById('comment-form');
const commentsList = document.getElementById('comments-list');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(form);

    fetch("", {
        method: "POST",
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${data.username}</strong>: ${data.text}`;
            commentsList.appendChild(li);

            form.reset();
        } else {
            alert("Error adding comment");
        }
    })
});
