import text_statistics


def test_sentences_split_1():
    res = text_statistics.sentences_split('Hello! How are you?')
    assert len(res) == 2
    assert res == ['Hello!', 'How are you?']


def test_sentences_split_2():
    res = text_statistics.sentences_split('Test?.. "Test, test, test!" Test...')
    assert len(res) == 3
    assert res == ['Test?..', '"Test, test, test!"', 'Test...']


def test_sentences_split_3():
    res = text_statistics.sentences_split('E. G. Brendon. Dr. Bro! Mr.Fento, \'test!..\'')
    assert len(res) == 3
    assert res == ['E. G. Brendon.', 'Dr. Bro!', 'Mr. Fento, \'test!..\'']


def test_sentences_amount_1():
    sent = text_statistics.sentences_split('Mr.Mia and J.K. Samuel! How are you?.. I\'m fine!')
    res = text_statistics.sentences_amount(sent)
    assert res == 3


def test_non_declarative_sentences_amount_1():
    sent = text_statistics.sentences_split('Test!.. Test... Test. Test?.. Test! Test test test.')
    res = text_statistics.non_declarative_sentences_amount(sent)
    assert res == 3


def test_average_sentence_length_1():
    sent = text_statistics.sentences_split('Test!.. Test... Test Test?.. Test test test.')
    res = text_statistics.average_sentence_length(sent)
    assert res == 7


def test_average_word_length_1():
    res = text_statistics.average_word_length('Test test. testing')
    assert res == 5


def test_top_n_grams_1():
    sent = text_statistics.sentences_split('Ment tot. Ment tot ment tot ment bra bru bra tot bra bru. Bru bra bru!..')
    res = text_statistics.top_n_grams(5, 2, sent)
    assert res == {"('ment', 'tot')": 3, "('bra', 'bru')": 3, "('tot', 'ment')": 2, "('bru', 'bra')": 2, "('ment', 'bra')": 1}
