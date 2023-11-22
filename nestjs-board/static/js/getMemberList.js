function showMemberList(json) {
    let result = ''
    for (const element of json) {
        result += `
        <div class="member-table-element2">
            <div class="info2">
                <div class="username2">${element.NICKNAME}</div>
                <div class="email2">${element.EMAIL}</div>
                <div class="date2">${element.REGISTERTIME.split("T")[0]}</div>
            </div>
            <div class="line"></div>
        </div>`

    }
    document.getElementById("member-table-start").innerHTML = result;
}

function fetchMemberJson() {
    fetch(`/user`)
        .then(response => response.json())
        .then((json) => {
            showMemberList(json)
        })
        .catch(error => {
            console.error("fetch error:", error);
        });
}

fetchMemberJson();