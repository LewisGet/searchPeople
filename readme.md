# What this

this is a tool to search twitter open follower data,
and mapping a relationship network.

# Getting start

setting up config files

```sh
cp ember/_settings.py ember/settings.py
```

# Tests

```sh
python -m coverage run manage.py test

python -m coverage report
```

### without coverage

```sh
python manage.py test
```

# Twitter add entity javascript

```javascript
/** user object */
var user = {
    "display_name": document.querySelector("main h2").innerText,
    "twitter_id": window.location.href.replace("https://twitter.com/", "").replace("/following", "").replace("#endScroll", "")
};

/** scroll down to get all connect data */
var connect_users_object = [];

window.saveConnectData = function() {
    var connect_users_table = main.querySelector("section").querySelectorAll("div[data-testid=UserCell]");

    connect_users_table.forEach(function(user_profile) {
        connect_users_object.push({
            "display_name": user_profile.querySelector("span").innerText,
            "twitter_id": user_profile.querySelector("a").href.replace("https://twitter.com/", "")
        });
        user_profile.setAttribute("data-testid", "has_load");
    });
}

var main = document.querySelector("main");

h1 = document.createElement("h1");
h1.id = "endScroll";
linkTag = document.createElement("a");
linkTag.href = "#endScroll";

main.appendChild(h1);
main.appendChild(linkTag);

for (var i = 0; i < 100; i++)
{
    setTimeout(function(){
        window.saveConnectData();
        linkTag.click();
    }, i * 500);
}

/** create url */
var url_base = "http://127.0.0.1:8000/add?";
var url = url_base + "display_name=" + user.display_name + "&";
url = url + "twitter_id=" + user.twitter_id + "&";

var connects_id = [];

connect_users_object.forEach(function(u) {
    connects_id.push(u.twitter_id);
});

var connects_id_str =  connects_id.join(",");

url = url + "connects_id=" + connects_id_str;

addLinkTag = document.createElement("a");
addLinkTag.href = url;
addLinkTag.target="_blank";
document.body.appendChild(addLinkTag);
addLinkTag.click();
```
