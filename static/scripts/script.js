var player;

function initialize() {

    updateTimerDisplay();
    updateProgressBar();

    clearInterval(time_update_interval);

    time_update_interval = setInterval(function () {
        updateTimerDisplay();
        updateProgressBar();
    }, 1000)

}

function onYouTubeIframeAPIReady() {
    player = new YT.Player('video-placeholder', {
        width: 600,
        height: 400,
        videoId: 'xchKBvIW66c',
        playerVars: {
            listType: 'playlist',
            color: 'white',
            list: 'PLo04flLN8lqT8jtPF8VuNoTaQfkfiYzQJ'
        },
        events: {
            onReady: initialize
        }
    });
}