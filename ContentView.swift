
//
//  ContentView.swift
//  MouthwashAppChallengeReal
//
//  Created by Krish Sathyan on 3/15/25.
//

import SwiftUI
import GoogleGenerativeAI
struct ContentView: View {
    let model = GenerativeModel(name: "gemini-2.0-flash", apiKey: APIKey.default)
    @State var userPrompt = ""
    @State var infoPrompt = ""
    @State var response = "How can I assist you today?"
    @State var isLoading  = false
    @State var firstname = ""
    @State var lastname = ""
    @State var age = ""
    @State var sleep = 0
    @State var city = 0
    @State var hours = ""
    @State var wearGlasses = false
    @State var activity = 0
    let cities = ["LA", "Moscow"]
    let activities = ["Gaming", "Work", "School", "Other"]
    var body: some View {
        NavigationView {
            Form{
                Section(header:
                            
                            Text("Personal info")){
                    TextField("What is your name", text: $firstname)
                    TextField("What is your last name", text: $lastname)
                    TextField("Age", text: $age)
                }
                
                Section(header: Text("Wears Glasses/Contacts")){
                    Toggle("Wears?", isOn: $wearGlasses)
                }
                

                
                Section(header: Text("Iphone info")){

                    TextField("Hours on iphone", text: $hours)
                
                }
                
                Section(header: Text("What do you do mostly on your phone?")){
                    
                }
                
                Section(){
                    Picker("Activity", selection: $activity){
                        ForEach(activities.indices, id: \.self) {i in
                            Text(self.activities[i])
                        }
                    }
                    
                    .pickerStyle(.segmented)
                }
                
                Section(header: Text("Submit")){
                    Button("Submit"){
                        print(firstname + " \(wearGlasses)")
                        if (wearGlasses) {
                            infoPrompt = "Give me tips on how to avoid screen time. I wear glasses. I am " + age + " years old. I also spend " + hours + " on my phone."
                        }
                        else{
                            infoPrompt = "Give me tips on how to avoid screen time. I don't wear glasses. I am " + age + " years old. I also spend " + hours + " on my phone."
                        }

                        Task{
                            do{
                                let result = try await model.generateContent(infoPrompt)
                                isLoading = false
                                response = result.text ?? "No Response found"
                                userPrompt = ""
                            }catch{
                                response = "Something went wrong\n\(error.localizedDescription)"
                            }
                                
                        }
                       
                    }
                }
                
                if isLoading {
                    ProgressView()
                        .progressViewStyle(CircularProgressViewStyle(tint: .indigo))
                        .scaleEffect(4)
                }
                
                Section(header: Text("Ai")){
                    Text(response)
                        .font(.title)
                }
                
                
                
                .navigationTitle("Information Form")
            }
            
            
                
        }
        
       
        
    }
    func generateResponse(){
        isLoading = true
        response = ""
        Task{
            do{
                let result = try await model.generateContent(userPrompt)
                isLoading = false
                response = result.text ?? "No Response found"
                userPrompt = ""
            }catch{
                response = "Something went wrong\n\(error.localizedDescription)"
            }
                
        }
    }
}

#Preview {
    ContentView()
}
