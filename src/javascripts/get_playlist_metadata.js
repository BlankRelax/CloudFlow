clearInterval(goToBottom);
let arrayVideos = [];
console.log('\n'.repeat(50));
const links = document.querySelectorAll('a');
for (const link of links) {
if (link.id === "video-title") {
    link.href = link.href.split('&list=')[0];
    arrayVideos.push(link.title + ';' + link.href);
    console.log(link.title + '\t' + link.href);
}
}