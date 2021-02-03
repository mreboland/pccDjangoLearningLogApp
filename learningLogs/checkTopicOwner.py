def checkTopicOwner():
    if topic.owner != request.user:
        raise Http404
