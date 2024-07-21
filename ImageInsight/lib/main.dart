import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ImageInsight',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ImageInsightHomePage(),
    );
  }
}

class ImageInsightHomePage extends StatefulWidget {
  @override
  _ImageInsightHomePageState createState() => _ImageInsightHomePageState();
}

class _ImageInsightHomePageState extends State<ImageInsightHomePage> {
  File? _image;

  Future<void> _getImageFromGallery() async {
    final picker = ImagePicker();
    final pickedFile = await picker.getImage(source: ImageSource.gallery);

    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
      } else {
        print('No image selected.');
      }
    });
  }

  Future<void> _uploadImage() async {
    if (_image == null) {
      print('No image selected.');
      return;
    }

    final url = 'http://localhost:5000/predict';  // Replace with your backend URL
    var request = http.MultipartRequest('POST', Uri.parse(url));
    request.files.add(await http.MultipartFile.fromPath('image', _image!.path));

    try {
      var response = await request.send();
      if (response.statusCode == 200) {
        var jsonResponse = await response.stream.bytesToString();
        var prediction = jsonDecode(jsonResponse);
        print('Prediction: $prediction');
        // Display the prediction in your app UI
      } else {
        print('Failed to upload image. Error: ${response.reasonPhrase}');
      }
    } catch (e) {
      print('Error uploading image: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image Insight'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _image == null
                ? Text('No image selected.')
                : Image.file(_image!),
            SizedBox(height: 20.0),
            ElevatedButton(
              onPressed: _getImageFromGallery,
              child: Text('Select Image'),
            ),
            SizedBox(height: 20.0),
            ElevatedButton(
              onPressed: _uploadImage,
              child: Text('Upload and Predict'),
            ),
          ],
        ),
      ),
    );
  }
}
