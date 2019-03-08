import VerificationServiceHttpClientHelper
import sys

def print_all_phrases(subscription_key):
    """Print all the supported phrases for the given subscription key.

    Arguments:
    subscription_key -- the subscription key string
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        subscription_key)

    phrases = helper.get_all_phrases("en-US")

    print("Supported phrases:")
    for phrase in phrases:
        print(" '{}'".format(phrase))

    return phrases

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python PrintAllPhrases.py <subscription_key>')
        print('\t<subscription_key> is the subscription key for the service')
        sys.exit('Error: Incorrect Usage.')

    print_all_phrases(sys.argv[1])
