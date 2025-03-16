//
//  ApiKey.swift
//  MOUTHWASREALREALREAL
//
//  Created by Krish Sathyan on 3/15/25.
//


import Foundation

enum APIKey{
    
    static var `default`: String{
        guard let filePath = Bundle.main.path(forResource: "GenerativeAI-Info", ofType:"plist")
        else{
            fatalError("Couldn't find file 'Generative AI - Info.plist'.")
        }
        
        let plist = NSDictionary(contentsOfFile: filePath)
        guard let value = plist?.object(forKey: "API_KEY") as? String else{
            fatalError("Couldn't find file 'api key'.")
        }
        
        if value.starts(with: "_"){
            fatalError(
                "Follow instructions"
            )
        }
        return value
    }
}
