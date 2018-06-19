import json
import pickle


def limitDatSet(dataset):
    total_topics = 0
    total_questions = 0
    squad_json = []

    for topic in dataset:
        total_topics += 1
        # Iterate through every text passage in the topic
        for passage in topic['paragraphs']:
            # Iterate through every question/answer pairs in the passage
            for qas in passage['qas']:
                total_questions += 1
                text_question_pair = {'topic': topic['title'], 'paragraph': passage['context'],
                                      'question': qas['question']}
                # Append the title
                # Append the text paragraph
                # Append the question
                # Iterate through available answers
                answers = []
                for answer in qas['answers']:
                    if total_topics < 100:
                        answers.append(answer['text'])
                # And append them all together
                        text_question_pair['answers'] = answers

                # Append found dictionary to the full parsed dataset array
                        squad_json.append(text_question_pair)

    print('Found ' + str(total_topics) + ' topics in total.')
    print('Found ' + str(total_questions) + ' questions in total.')
    return squad_json


squad_train_filepath = 'data/testing/train-v1.1.json'
save_path = 'data/testing/parsed_train_data.json'

# Load squad train dataset
train_json = json.load(open(squad_train_filepath, 'r'))
train_dataset = train_json['data']

parsed_train_squad = limitDatSet(train_dataset)
json.dump(parsed_train_squad, open(save_path, 'w'))

# ==============================================================================
# # PARSE AND SAVE DEV DATA
# ==============================================================================
# Filepath to squad dataset and path where to save the parsed dataset
squad_dev_filepath = 'data/testing/dev-v1.1.json'
save_path = 'data/testing/parsed_dev_data.json'

# Load squad dev dataset
dev_json = json.load(open(squad_dev_filepath, 'r'))
dev_dataset = dev_json['data']

parsed_dev_squad = limitDatSet(dev_dataset)
json.dump(parsed_dev_squad, open(save_path, 'w'))

# ======================================================================
# Extract paragraph/questions pairs from Stanford's QUAD database
# ======================================================================

train_filepath = 'data/testing/parsed_train_data.json'
dev_filepath = 'data/testing/parsed_dev_data.json'

train_set = json.load(open(train_filepath, 'r'))
dev_set = json.load(open(dev_filepath, 'r'))

train_paragraphs = []
train_questions = []
for section in train_set:
    if section < 100:
        train_paragraphs.append(section['paragraph'])
        train_questions.append(section['question'])

dev_paragraphs = []
dev_questions = []
for section in dev_set:
    if section < 100:
        dev_paragraphs.append(section['paragraph'])
        dev_questions.append(section['question'])

assert len(train_paragraphs) == len(train_questions)
assert len(dev_paragraphs) == len(dev_questions)

# ==============================================================================
# # Pickle up the extracted lists of questions/anserws pairs
# ==============================================================================
def save_pickle_file(data, filename):
    """Saves the data into pickle format"""
    save_documents = open('data/testing/' + filename + '.pickle', 'wb')
    pickle.dump(data, save_documents)
    save_documents.close()


save_pickle_file(train_paragraphs, 'train_squad_paragraphs')
save_pickle_file(train_questions, 'train_squad_questions')
save_pickle_file(dev_paragraphs, 'dev_squad_paragraphs')
save_pickle_file(dev_questions, 'dev_squad_questions')
