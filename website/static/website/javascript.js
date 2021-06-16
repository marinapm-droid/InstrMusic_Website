function successfull() {
    alert('Form submitted succesfully!')
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('form').onsubmit = successfull;
});

document.addEventListener('DOMContentLoaded', () => { //

    document.querySelector('#participate').onsubmit = function () {
        let participant_name = document.querySelector('#id_name').value;
        alert(`Have fun ${participant_name}!`);
    }
});


document.addEventListener('DOMContentLoaded', () => { //

    document.querySelector('#login').onsubmit = function () {
        localStorage.setItem("username", document.querySelector('#login_username').value);
        let username = document.querySelector('#login_username').value;
        alert(`Welcome ${username}!`);
    }
});

document.addEventListener('DOMContentLoaded', () => { //
    document.querySelector('#logout').addEventListener("click", e => {
        let username = localStorage.getItem("username");
        alert(`Goodbye ${username}!`);
    });
});

function showSection(section) {

    window.onpopstate = function (event) {
        console.log(event.state.section);
        showSection(event.state.section);
    }


    fetch(`/sections/${section}`)
        .then(response => response.text())
        .then(text => {
            console.log(text);
            document.querySelector('#section').innerHTML = text;
        });

}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.button').forEach(button => {
        button.onclick = function () {
            const section = this.dataset.section;
            history.pushState({section: section}, "", `section${section}`);
            showSection(section);
        };
    });
});

document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('id_email').onfocus = () => {
        document.getElementById('id_email').setAttribute('class', 'focusinput');
    };


    document.getElementById('id_email').onblur = () => {
        document.getElementById('id_email').setAttribute('class', 'input');
    };

    document.getElementById('id_question2').onfocus = () => {
        document.getElementById('id_email').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_question2').onblur = () => {
        document.getElementById('id_email').setAttribute('class', 'input');
    };

});


document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('id_question2').onfocus = () => {
        document.getElementById('id_question2').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_question2').onblur = () => {
        document.getElementById('id_question2').setAttribute('class', 'input');
    };

});


document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('id_question8').onfocus = () => {
        document.getElementById('id_question8').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_question8').onblur = () => {
        document.getElementById('id_question8').setAttribute('class', 'input');
    };

    document.getElementById('id_question9').onfocus = () => {
        document.getElementById('id_question9').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_question9').onblur = () => {
        document.getElementById('id_question9').setAttribute('class', 'input');
    };


    document.getElementById('id_question10').onfocus = () => {
        document.getElementById('id_question10').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_question10').onblur = () => {
        document.getElementById('id_question10').setAttribute('class', 'input');
    };
});

document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('id_subject').onfocus = () => {
        document.getElementById('id_subject').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_subject').onblur = () => {
        document.getElementById('id_subject').setAttribute('class', 'input');
    };

});



document.addEventListener('DOMContentLoaded', function () {

      document.getElementById('id_date').onfocus = () => {
        document.getElementById('id_date').setAttribute('class', 'focusinput');
    };
       document.getElementById('id_date').onblur = () => {
        document.getElementById('id_date').setAttribute('class', 'input');
    };


});

document.addEventListener('DOMContentLoaded', function () {

     document.getElementById('id_question7').onfocus = () => {
        document.getElementById('id_question7').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_question7').onblur = () => {
        document.getElementById('id_question7').setAttribute('class', 'input');
    };

});


document.addEventListener('DOMContentLoaded', function () {

        document.getElementById('id_instrument').onfocus = () => {
        document.getElementById('id_instrument').setAttribute('class', 'focusinput');
    };
       document.getElementById('id_instrument').onblur = () => {
        document.getElementById('id_instrument').setAttribute('class', 'input');
    };

});


document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('id_title').onfocus = () => {
        document.getElementById('id_title').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_title').onblur = () => {
        document.getElementById('id_title').setAttribute('class', 'input');
    };


    document.getElementById('id_description').onfocus = () => {
        document.getElementById('id_description').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_description').onblur = () => {
        document.getElementById('id_description').setAttribute('class', 'input');
    };

    document.getElementById('id_time').onfocus = () => {
        document.getElementById('id_time').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_time').onblur = () => {
        document.getElementById('id_time').setAttribute('class', 'input');
    };

});


document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('id_name').onfocus = () => {
        document.getElementById('id_name').setAttribute('class', 'focusinput');
    };
    document.getElementById('id_name').onblur = () => {
        document.getElementById('id_name').setAttribute('class', 'input');
    };

    document.getElementById('id_surname').onblur = () => {
        document.getElementById('id_surname').setAttribute('class', 'input');
    };
    document.getElementById('id_surname').onfocus = () => {
        document.getElementById('id_surname').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_cell_number').onblur = () => {
        document.getElementById('id_cell_number').setAttribute('class', 'input');
    };

    document.getElementById('id_cell_number').onfocus = () => {
        document.getElementById('id_cell_number').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_birthday').onfocus = () => {
        document.getElementById('id_birthday').setAttribute('class', 'focusinput');
    };


    document.getElementById('id_birthday').onblur = () => {
        document.getElementById('id_birthday').setAttribute('class', 'input');
    };


    document.getElementById('id_message').onfocus = () => {
        document.getElementById('id_message').setAttribute('class', 'focusinput');
    };

    document.getElementById('id_message').onblur = () => {
        document.getElementById('id_message').setAttribute('class', 'input');
    };

});