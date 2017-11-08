from dialogue import DialogueLineNoResponse, Dialogue, DialogueLineBinaryResponse, DialogueLineAnyResponse


def get_dialogue_for_label(label):
    # type: (str) -> Dialogue
    """
    Get the dialogue that can be used when CommU sees an object.
    :param label:   The label assigned by the ssd network
    :return:        The pre-scripted Dialogue concerning the object.
    """
    return dialogue_map[label]


dialogue_map = {
    'aeroplane': None,
    'bicycle': None,
    'bird': None,
    'boat': None,
    'bottle':
        Dialogue(
            DialogueLineAnyResponse("What are you drinking?",
                DialogueLineNoResponse("That sounds tasty",
                    DialogueLineBinaryResponse("Do you like orange juice?",
                        next_line_yes= DialogueLineNoResponse("That's nice! Me too!", None),
                        next_line_no = DialogueLineNoResponse("That's a shame. I like it a lot", None)
                    )
                )
            )
        ),
    'bus': None,
    'car': None,
    'cat':
        Dialogue(
            DialogueLineNoResponse("I see you have a cat",
                DialogueLineNoResponse("I love cats!",
                    DialogueLineNoResponse("I especially like black cats",
                        DialogueLineBinaryResponse("Do you like cats too?",
                            next_line_yes= DialogueLineNoResponse("Good!", None),
                            next_line_no=  DialogueLineNoResponse("That's a shame", None)
                        )
                    )
                )
            )
        ),
    'chair':
        Dialogue(
            DialogueLineNoResponse("That's a nice chair.",
                DialogueLineNoResponse("I've always liked that kind of chair",
                    DialogueLineBinaryResponse("Do you like it?",
                        next_line_yes = DialogueLineNoResponse("That's nice", None),
                        next_line_no = DialogueLineNoResponse("I still think it's cool", None)
                    )
                )
            )
        ),
    'cow': None,
    'diningtable':
        Dialogue(
            DialogueLineBinaryResponse("I see you have a table. Do you like it?",
                next_line_yes = DialogueLineNoResponse("Yeah, me too!", None),
                next_line_no = DialogueLineNoResponse("I think it seems somewhat inconvenient as well", None)
            )
        ),
    'dog': None,
    'horse': None,
    'motorbike': None,
    'person':
        Dialogue(
            DialogueLineNoResponse("Hey there, nice to meet you!",
                DialogueLineAnyResponse("Can I ask you a question?",
                    DialogueLineBinaryResponse("Have you ever talked to a robot before?",
                        next_line_yes = DialogueLineAnyResponse("Cool, what was his name?",
                            DialogueLineNoResponse("I met him yesterday, he's such a nice person!",
                                DialogueLineNoResponse("Let's have a chat.", None)
                            )
                        ),
                        next_line_no  = DialogueLineNoResponse("Well, there's a first time for everything.",
                            DialogueLineNoResponse("Let's have a chat.", None)
                        )
                    )
                )
            )
        ),
    'pottedplant':
        Dialogue(
            DialogueLineNoResponse("Nice plant you have there",
                DialogueLineNoResponse("I like it a lot", None)
            )
        ),
    'sheep': None,
    'sofa':
        Dialogue(
            DialogueLineNoResponse("I love sofas!",
                DialogueLineBinaryResponse("Did you know that sofas can also be used to sleep on?",
                    next_line_yes = DialogueLineNoResponse("I won't be able to tell you anything new today then.", None),
                    next_line_no  = DialogueLineNoResponse("You learn something new every day.", None)
                )
            )
        ),
    'train': None,
    'tvmonitor':
        Dialogue(
            DialogueLineAnyResponse("What are you using that screen over there for?",
                DialogueLineNoResponse("Cool, I like to do that too.", None)
            )
        ),
}