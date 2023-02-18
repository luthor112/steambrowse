// ==UserScript==
// @namespace	luthor.local
// @name     	steambrowse
// @version  	1
// @grant    	none
// @match    	https://steamcommunity.com/workshop/browse/*
// ==/UserScript==

// CONFIGURATION
var server_url = 'http://127.0.0.1:8080/browse'

var itemList = document.getElementsByClassName('workshopItem');
for (let i = 0; i < itemList.length; i++) {
    itemLink = itemList[i].getElementsByClassName('ugc')[0];
    itemLink.href = server_url + '?appid=' + itemLink.attributes['data-appid'].nodeValue + '&itemid=' + itemLink.attributes['data-publishedfileid'].nodeValue
}