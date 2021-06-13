document.addEventListener("DOMContentLoaded", (event) => {
    const registerMember = (url, data) => {
        let xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState === 4) {
                const response = this.responseText !== "" ? JSON.parse(this.responseText) : {};
                if(response['errors']) {
                    processErrors(response['errors']);
                }
                if (response['status'] === 'success') {
                    addMember(response['user_data']);
                }
                processMessage(response['status'], response['message']);
            }
        };
        xmlhttp.open("POST", url, true);
        xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xmlhttp.send(data);
    };
    const addMember = (member_data) => {
        const member_table = document.querySelector('.members');
        member_table.innerHTML += `
            <tr>
                <td>${member_data['index']}</td>
                <td>${member_data['name']}</td>
                <td>${member_data['email']}</td>
                <td>${member_data['registration_date']}</td>
            </tr>
        `;
    };

    const processMessage = (status, message) => {
        const messages = document.querySelector('.messages');
        messages.innerHTML = '';
        messages.innerHTML += `<div class="${status}">${message}
            <span class="icon-cross" onclick="parentElement.remove()"><i class="fas fa-times"></i></span>
        </div>`;
    };

    const processErrors = (errors) => {
        const email_field = document.querySelector('input[name=email]');
        let name_field = document.querySelector('input[name=name]');
        if(errors['name']) {
            name_field.classList.add('error');
            for (const error in errors['name']) {
                name_field.parentElement.querySelector('.errors').innerHTML += `<li>${errors['name'][error]}</li>`;
            }
        }
        if(errors['email']) {
            email_field.classList.add('error');
            for (const error in errors['email']) {
                email_field.parentElement.querySelector('.errors').innerHTML += `<li>${errors['email'][error]}</li>`;
            }
        }
    };

    const clearErrors = () => {
        document.querySelectorAll('ul.errors').forEach((err_block) => {
            err_block.innerHTML = '';
            err_block.parentElement.querySelector('input').classList.remove('error');
        });
    };

    const btn = document.querySelector('.member-add');
    btn.addEventListener('click', (event) => {
        event.preventDefault();
        const name_field = document.querySelector('input[name=name]');
        const email_field = document.querySelector('input[name=email]');
        clearErrors();
        if (!name_field.value) {
            processErrors({'name': ['Enter name']})
            return;
        }
        if (!email_field.value) {
            processErrors({'email': ['Enter email']})
            return;
        }
        registerMember(
            event.target.dataset.url,
            'name=' + encodeURIComponent(name_field.value) +
            '&email=' + encodeURIComponent(email_field.value) +
            '&csrf_token=' + encodeURIComponent(document.querySelector('input[name=csrf_token]').value)
        );
    })

    const clear_btn = document.querySelector('.clear-btn');
    clear_btn.addEventListener('click', (event) => {
        event.preventDefault();
        document.querySelectorAll('input[type=text]').forEach((field) => {
           field.value = '';
        })
        clearErrors();
    });
});