import Foundation
import SwiftyJSON

struct DemoModel {
  let stringKey: String
  let boolKey: Bool
  let intKey: Int

  static func produce(from json: JSON) -> DemoModel {
    return DemoModel(stringKey: json["stringKey"].stringValue,
                     boolKey: json["boolKey"].boolValue,
                     intKey: json["intKey"].intValue)
  }
}

struct DemoModel2 {
  let stringKey: String
  let boolKey: Bool

  static func produce(from json: JSON) -> DemoModel2 {
    return DemoModel2(stringKey: json["stringKey"].stringValue,
                      boolKey: json["boolKey"].boolValue)
  }
}

struct DemoModel3 {
  let stringKey: String
  let boolKey: Bool
  let otherDemo: DemoModel2

  static func produce(from json: JSON) -> DemoModel3 {
    return DemoModel3(stringKey: json["stringKey"].stringValue,
                      boolKey: json["boolKey"].boolValue,
                      otherDemo: DemoModel2.produce(from: json["otherDemo"]))
  }
}

struct DemoModel4 {
  let stringKey: String
  let boolKey: Bool
  let otherDemo: DemoModel2
  let otherDemo2: DemoModel3

  static func produce(from json: JSON) -> DemoModel4 {
    return DemoModel4(stringKey: json["stringKey"].stringValue,
                      boolKey: json["boolKey"].boolValue,
                      otherDemo: DemoModel2.produce(from: json["otherDemo"]),
                      otherDemo2: DemoModel3.produce(from: json["otherDemo2"]))
  }
}

