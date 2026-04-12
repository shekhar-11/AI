WHy not ANN?
Because ANN is not designed to handle sequential data effectively. ANN processes each input independently and does not have the capability to retain information from previous inputs, which is crucial for tasks involving sequences, such as language modeling or time series prediction.
All the input of the sentence is sent all at once in ANN making the sequence break and it cannot capture the dependencies between words in a sentence.



While in RNN , the hidden state is updated at each time step, allowing the network to maintain a memory of previous inputs. This makes RNNs well-suited for tasks that involve sequential dependencies, as they can capture the context and relationships between elements in a sequence.


So lets say if the word "the" is sent first at t=T1 timestamp, then in T2 the other word is sent , and the same hidden layer has the information of the word "the" and now it received the second word and it can capture the relationship between the two words and the context of the sentence. This is why RNNs are preferred for sequential data tasks, as they can effectively model the dependencies and relationships within sequences, while ANN cannot.



Consider the pdf, for visual representation.