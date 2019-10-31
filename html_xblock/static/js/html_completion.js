function HTML5CompletionXBlock(runtime, element, data) {
    /*
    Add dummy #complete element with event listener for sending the POST to the custom `complete` handler.
     */
    // Add dummy element.
    var main = document.getElementById("main");
    var tracker = document.createElement("div");
    tracker.id = "complete";
    main.appendChild(tracker);

    // Add `complete` handler to the dummy element.
    tracker.addEventListener("click", function () {
        var handlerUrl = runtime.handlerUrl(element, 'complete');

        $.post(handlerUrl, JSON.stringify(data)).done(function (response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}
