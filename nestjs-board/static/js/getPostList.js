function showPosts(json) {
    let result = ''
    for (const element of json) {
        result += `
        <div class="post-table-elements2">
            <div class="text2">
                <div class="title2" onclick="location.href='/board/detail/?pk=${element.pk}';">
                    <div class="text3">${element.title}</div>
                </div>
                <div class="writer2">${element.nickname}</div>
                <div class="date2">${element.registertime.split("T")[0]}</div>
                <div class="view2">${element.view}</div>
            </div>
            <div class="line"></div>
        </div>`
        
    }
    document.getElementById("post-start").innerHTML = result;
}

function fetchPostJson() {
    fetch(`/board`)
        .then(response => response.json())
        .then((json) => {
            showPosts(json)
        })
        .catch(error => {
            console.error("fetch error:", error);
        });
}

fetchPostJson();