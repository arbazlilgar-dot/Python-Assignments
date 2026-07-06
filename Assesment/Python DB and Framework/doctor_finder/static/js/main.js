// Client-side Form Validation
document.addEventListener('DOMContentLoaded', () => {
    
    const validateEmail = (email) => {
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            );
    };

    const signupForm = document.getElementById('signupForm');
    if(signupForm) {
        signupForm.addEventListener('submit', (e) => {
            let valid = true;
            
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const p1 = document.getElementById('password').value;
            const p2 = document.getElementById('confirm_password').value;

            // Simple resets
            document.querySelectorAll('.error-msg').forEach(el => el.style.display = 'none');

            if(name.length < 3) {
                document.getElementById('nameErr').style.display = 'block';
                document.getElementById('nameErr').innerText = "Name must be at least 3 characters";
                valid = false;
            }
            if(!validateEmail(email)) {
                document.getElementById('emailErr').style.display = 'block';
                document.getElementById('emailErr').innerText = "Invalid email address";
                valid = false;
            }
            if(phone.length < 10) {
                document.getElementById('phoneErr').style.display = 'block';
                document.getElementById('phoneErr').innerText = "Phone number must be at least 10 digits";
                valid = false;
            }
            if(p1.length < 6) {
                document.getElementById('passErr').style.display = 'block';
                document.getElementById('passErr').innerText = "Password must be at least 6 characters";
                valid = false;
            }
            if(p1 !== p2) {
                document.getElementById('confirmErr').style.display = 'block';
                document.getElementById('confirmErr').innerText = "Passwords do not match";
                valid = false;
            }

            if(!valid) e.preventDefault();
        });
    }
});

// AJAX Functions for Admin CRUD
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function openAddDoctorModal() {
    document.getElementById('doctorModal').style.display = 'flex';
}

function closeDoctorModal() {
    document.getElementById('doctorModal').style.display = 'none';
    document.getElementById('ajaxDoctorForm').reset();
}

function submitAjaxDoctorForm(e) {
    e.preventDefault();
    const formData = new FormData(document.getElementById('ajaxDoctorForm'));
    
    const csrftoken = getCookie('csrftoken');
    fetch('/ajax/doctors/add/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if(data.status === 'success') {
            alert('Doctor added successfully!');
            location.reload(); // Refresh to see changes, or dynamically append row
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred.');
    });
}

function deleteDoctor(id) {
    if(confirm("Are you sure you want to delete this doctor?")) {
        const csrftoken = getCookie('csrftoken');
        fetch('/ajax/doctors/delete/' + id + '/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .then(response => response.json())
        .then(data => {
            if(data.status === 'success') {
                alert('Doctor deleted!');
                document.getElementById('doc-row-'+id).remove();
            }
        });
    }
}
