from dialogue_action import *
from __init__ import *


class DialogueLibraryTalk(DialogueLibrary):
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
        return Dialogue(DialogueLibraryTalk.dialogue_map[topic])

    dialogue_map = {
        'aeroplane': None,
        'bicycle':
            DialogueActionTalkNoResponse(
                utterance   = "Hey, a bike!",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "I wonder where he's going.",
                    cancelable  = True,
                    next_action = None
                )
            ),
        'bird':
            DialogueActionTalkNoResponse(
                utterance   = "Do you know what kind of bird that is?",
                cancelable  = False,
                next_action = DialogueActionSleep(
                    sleep_time  = 3,
                    cancelable  = False,
                    next_action = DialogueActionTalkNoResponse(
                        utterance   = "Huh, interesting.",
                        cancelable  = True,
                        next_action = None
                    )
                )
            ),
        'boat':
            DialogueActionLook(
                look_type   = DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER,
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "I didn't think I would see a boat around here.",
                    cancelable  = True,
                    next_action = DialogueActionTalkNoResponse(
                        utterance   = "What a coincidence.",
                        cancelable  = True,
                        next_action = None
                    )
                ),
            ),
        'bottle':
            DialogueActionTalkNoResponse(
                utterance   = "What are you drinking?",
                cancelable  = False,
                next_action =  DialogueActionSleep(
                    sleep_time  = 2,
                    cancelable  = False,
                    next_action = DialogueActionTalkNoResponse(
                        utterance   = "That sounds tasty",
                        cancelable  = True,
                        next_action = DialogueActionTalkBinaryResponse(
                            utterance       = "Do you like orange juice?",
                            cancelable      = False,
                            next_action_yes = DialogueActionTalkNoResponse(
                                utterance   = "That's nice! Me too!",
                                cancelable  = True,
                                next_action = None
                            ),
                            next_action_no  = DialogueActionTalkNoResponse(
                                utterance   = "That's a shame. I like it a lot",
                                cancelable  = True,
                                next_action = None
                            )
                        )
                    )
                )
            ),
        'bus':
            DialogueActionTalkNoResponse(
                utterance   = "I wonder where that bus is going.",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "Do you know where it's going?",
                    cancelable  = False,
                    next_action = DialogueActionSleep(
                        sleep_time  = 2,
                        cancelable  = False,
                        next_action = DialogueActionTalkNoResponse(
                            utterance   = "Cool, I'd like to go there too!",
                            cancelable  = True,
                            next_action = None
                        )
                    )
                )
            ),
        'car':
            DialogueActionTalkNoResponse(
                utterance   = "Nice car!",
                cancelable  = True,
                next_action = None
            ),
        'cat':
            DialogueActionTalkNoResponse(
                utterance   = "I see you have a cat",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "I love cats!",
                    cancelable  = True,
                    next_action = DialogueActionTalkNoResponse(
                        utterance   = "I especially like black cats",
                        cancelable  = True,
                        next_action = DialogueActionTalkBinaryResponse(
                            utterance     = "Do you like cats too?",
                            cancelable    = False,
                            next_action_yes = DialogueActionTalkNoResponse(
                                utterance   = "Good!",
                                cancelable  = True,
                                next_action = None
                            ),
                            next_action_no  = DialogueActionTalkNoResponse(
                                utterance   = "That's a shame",
                                cancelable  = True,
                                next_action = None
                            )
                        )
                    )
                )
            ),
        'chair':
            DialogueActionTalkNoResponse(
                utterance   = "That's a nice chair.",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "I've always liked that kind of chair",
                    cancelable  = True,
                    next_action = DialogueActionTalkBinaryResponse(
                        utterance       = "Do you like it?",
                        cancelable      = False,
                        next_action_yes = DialogueActionTalkNoResponse(
                            utterance   = "That's nice",
                            cancelable  = True,
                            next_action = None
                        ),
                        next_action_no  = DialogueActionTalkNoResponse(
                            utterance   = "I still think it's cool",
                            cancelable  = True,
                            next_action = None
                        )
                    )
                )
            ),
        'cow': None,
        'diningtable':
            DialogueActionTalkBinaryResponse(
                utterance       = "I see you have a table. Do you like it?",
                cancelable      = False,
                next_action_yes = DialogueActionTalkNoResponse(
                    utterance   = "Yeah, me too!",
                    cancelable  = True,
                    next_action = None
                ),
                next_action_no  = DialogueActionTalkNoResponse(
                    utterance   = "I think it seems somewhat inconvenient as well",
                    cancelable  = True,
                    next_action = None
                )
            ),
        'dog':
            DialogueActionTalkNoResponse(
                utterance   = "That's a nice dog!",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "Can I pet it?",
                    cancelable  = True,
                    next_action = None
                )
            ),
        'horse': None,
        'motorbike':
            DialogueActionTalkNoResponse(
                utterance   = "Motorbikes look so cool!",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "They're way too scary for me though!",
                    cancelable  = True,
                    next_action = None
                )
            ),
        'person':
            DialogueActionTalkNoResponse(
                utterance   = "Hey there, nice to meet you!",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "Can I ask you a question?",
                    cancelable  = False,
                    next_action = DialogueActionSleep(
                        sleep_time  = 2,
                        cancelable  = False,
                        next_action = DialogueActionTalkBinaryResponse(
                            utterance     = "Have you ever talked to a robot before?",
                            cancelable    = False,
                            next_action_yes = DialogueActionTalkNoResponse(
                                utterance   = "Cool, what was his name?",
                                cancelable  = False,
                                next_action = DialogueActionTalkNoResponse(
                                    utterance   = "I met him yesterday, he's such a nice person!",
                                    cancelable  = True,
                                    next_action = DialogueActionTalkNoResponse(
                                        utterance   = "Let's have a chat.",
                                        cancelable  = True,
                                        next_action = None
                                    )
                                )
                            ),
                            next_action_no  = DialogueActionTalkNoResponse(
                                utterance   = "Well, there's a first time for everything.",
                                cancelable  = True,
                                next_action = DialogueActionTalkNoResponse(
                                    utterance   = "Let's have a chat.",
                                    cancelable  = True,
                                    next_action = None
                                )
                            )
                        ),
                    )
                )
            ),
        'pottedplant':
            DialogueActionTalkNoResponse(
                utterance   = "Nice plant you have there",
                cancelable  = True,
                next_action = DialogueActionTalkNoResponse(
                    utterance   = "I like it a lot",
                    cancelable  = True,
                    next_action = None
                )
            ),
        'sheep': None,
        'sofa':
            DialogueActionTalkNoResponse(
                utterance   = "I love sofas!",
                cancelable  = True,
                next_action = DialogueActionTalkBinaryResponse(
                    utterance       = "Did you know that sofas can also be used to sleep on?",
                    cancelable      = False,
                    next_action_yes = DialogueActionTalkNoResponse(
                        utterance   = "I won't be able to tell you anything new today then.",
                        cancelable  = True,
                        next_action = None
                    ),
                    next_action_no  = DialogueActionTalkNoResponse(
                        utterance   = "You learn something new every day.",
                        cancelable  = True,
                        next_action = None
                    )
                )
            ),
        'train': None,
        'tvmonitor':
            DialogueActionTalkNoResponse(
                utterance   = "What are you using that screen over there for?",
                cancelable  = False,
                next_action = DialogueActionSleep(
                    sleep_time  = 2,
                    cancelable  = False,
                    next_action = DialogueActionTalkNoResponse(
                        utterance   = "Cool, I like to do that too.",
                        cancelable  = True,
                        next_action = None
                    )
                )
            ),
    }