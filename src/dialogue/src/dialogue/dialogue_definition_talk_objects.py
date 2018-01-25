from dialogue import DialogueLineNoResponse, Dialogue, DialogueLineBinaryResponse, DialogueLineAnyResponse
from dialogue_manager import DialogueLibrary


class CommUDialogueLibrary(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object.
    """

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The pre-scripted Dialogue concerning the object.
        """
        return Dialogue(CommUDialogueLibrary.dialogue_map[topic])

    dialogue_map = {
        'aeroplane': None,
        'bicycle':
            DialogueLineNoResponse("Hey, a bike!", True,
                DialogueLineNoResponse("I wonder where he's going.", True, None)
            ),
        'bird':
            DialogueLineAnyResponse("Do you know what kind of bird that is?", False,
                DialogueLineNoResponse("Huh, interesting.", True, None)
            ),
        'boat':
            DialogueLineNoResponse("I didn't think I would see a boat around here.", True,
                DialogueLineNoResponse("What a coincidence.", True, None)
            ),
        'bottle':
            DialogueLineAnyResponse("What are you drinking?", False,
                DialogueLineNoResponse("That sounds tasty", True,
                    DialogueLineBinaryResponse("Do you like orange juice?", False,
                        next_line_yes= DialogueLineNoResponse("That's nice! Me too!", True, None),
                        next_line_no = DialogueLineNoResponse("That's a shame. I like it a lot", True, None)
                    )
                )
            ),
        'bus':
            DialogueLineNoResponse("I wonder where that bus is going.", True,
                DialogueLineAnyResponse("Do you know where it's going?", False,
                    DialogueLineNoResponse("Cool, I'd like to go there too!", True, None)
                )
            ),
        'car':
            DialogueLineNoResponse("Nice car!", True, None),
        'cat':
            DialogueLineNoResponse("I see you have a cat", True,
                DialogueLineNoResponse("I love cats!", True,
                    DialogueLineNoResponse("I especially like black cats", True,
                        DialogueLineBinaryResponse("Do you like cats too?", False,
                            next_line_yes= DialogueLineNoResponse("Good!", True, None),
                            next_line_no=  DialogueLineNoResponse("That's a shame", True, None)
                        )
                    )
                )
            ),
        'chair':
            DialogueLineNoResponse("That's a nice chair.", True,
                DialogueLineNoResponse("I've always liked that kind of chair", True,
                    DialogueLineBinaryResponse("Do you like it?", False,
                        next_line_yes = DialogueLineNoResponse("That's nice", True, None),
                        next_line_no = DialogueLineNoResponse("I still think it's cool", True, None)
                    )
                )
            ),
        'cow': None,
        'diningtable':
            DialogueLineBinaryResponse("I see you have a table. Do you like it?", False,
                next_line_yes = DialogueLineNoResponse("Yeah, me too!", True, None),
                next_line_no = DialogueLineNoResponse("I think it seems somewhat inconvenient as well", True, None)
            ),
        'dog':
            DialogueLineNoResponse("That's a nice dog!", True,
                DialogueLineNoResponse("Can I pet it?", True, None)
            ),
        'horse': None,
        'motorbike':
            DialogueLineNoResponse("Motorbikes look so cool!", True,
                DialogueLineNoResponse("They're way too scary for me though!", True, None)
            ),
        'person':
            DialogueLineNoResponse("Hey there, nice to meet you!", True,
                DialogueLineAnyResponse("Can I ask you a question?", False,
                    DialogueLineBinaryResponse("Have you ever talked to a robot before?", False,
                        next_line_yes = DialogueLineAnyResponse("Cool, what was his name?", False,
                            DialogueLineNoResponse("I met him yesterday, he's such a nice person!", True,
                                DialogueLineNoResponse("Let's have a chat.", True, None)
                            )
                        ),
                        next_line_no  = DialogueLineNoResponse("Well, there's a first time for everything.", True,
                            DialogueLineNoResponse("Let's have a chat.", True, None)
                        )
                    )
                )
            ),
        'pottedplant':
            DialogueLineNoResponse("Nice plant you have there", True,
                DialogueLineNoResponse("I like it a lot", True, None)
            ),
        'sheep': None,
        'sofa':
            DialogueLineNoResponse("I love sofas!", True,
                DialogueLineBinaryResponse("Did you know that sofas can also be used to sleep on?", False,
                    next_line_yes = DialogueLineNoResponse("I won't be able to tell you anything new today then.", True, None),
                    next_line_no  = DialogueLineNoResponse("You learn something new every day.", True, None)
                )
            ),
        'train': None,
        'tvmonitor':
            DialogueLineAnyResponse("What are you using that screen over there for?", False,
                DialogueLineNoResponse("Cool, I like to do that too.", True, None)
            ),
    }