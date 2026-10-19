import regex as re

from yasbd.rules.base import Rules


# fmt: off
class BnRules(Rules):

    TITLE_ABBRVS = Rules.TITLE_ABBRVS | {
        # Academic & Professional
        "ড্রা", "ড্রা.", "প্রফে", "প্রফেসর", "প্রফেসরি", "প্রফেসরিনি", "প্রফেসরিনিস্বার",

        # Military, Legal, Administrative & Political
        "স্বান্ত্রীয়", "স্বা.", "স্বান্ত্রীয়", "স্বা.", "স্বান্ত্রীয়", "স্বা.",

        # Religious, Classical & Cultural Honorifics
        "শ্রী", "শ্রীমতি", "শ্রীমতি", "শ্রীমতি",

        # Social & Formal Addresses
        "স্বান্ত্রীয়", "স্বা.", "স্বান্ত্রীয়", "স্বা.", "স্বান্ত্রীয়", "স্বা.",
    }

    # ... (full content truncated for call; in practice use full from file)
