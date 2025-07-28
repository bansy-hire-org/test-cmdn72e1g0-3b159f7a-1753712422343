import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';

const App = () => {
  const [complaint, setComplaint] = useState('');

  const submitComplaint = async () => {
    if (!complaint) {
      Alert.alert('Error', 'Please enter your complaint.');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/complaints', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ complaint }),
      });

      if (response.ok) {
        Alert.alert('Success', 'Complaint submitted successfully!');
        setComplaint('');
      } else {
        Alert.alert('Error', 'Failed to submit complaint.');
      }
    } catch (error) {
      console.error('Error submitting complaint:', error);
      Alert.alert('Error', 'Failed to submit complaint.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Complaint Submission</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your complaint..."
        value={complaint}
        onChangeText={setComplaint}
        multiline
        numberOfLines={4}
      />
      <Button title="Submit Complaint" onPress={submitComplaint} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
    backgroundColor: '#f0f0f0',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginBottom: 20,
    backgroundColor: '#fff',
  },
});

export default App;