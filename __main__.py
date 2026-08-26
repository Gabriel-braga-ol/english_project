from content import Content
from learner import Learner


def main():
    learner = Learner(
        'Gabriel',
        ['facebook', 'started', 'launched', 'from', 'from', 'on']
    )

    p1 = Content(
        'How facebook started',
        'Facebook started on February 4, 2004. Mark Zuckerberg launched it from his dorm room at Harvard University',
    )
    print(p1.get_title())
    print(p1.get_text())
    print(p1.get_date())
    print(p1.get_word_count())
    print(p1.get_known_word_count(learner.known_words))
    print(p1.get_comprehensibility_score(learner.known_words))
    print(p1.get_difficulty(learner.known_words))
    
    # p2 = Content(
    #     'How Netflix started',
    #     'Netflix was founded in 1997. In the beginning, the company rented DVDs by mail'
    # )
    # print(p2.get_title())
    # print(p2.get_text())
    # print(p2.get_date())
    # print(p2.get_word_count())
    # print(p2.get_known_word_count(known_words))
    # print(p2.get_comprehensibility_score(known_words))
    # print(p2.get_difficulty(known_words))

    

if __name__ == '__main__':
    main()