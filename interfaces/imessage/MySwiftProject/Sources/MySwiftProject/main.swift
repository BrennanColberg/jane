import Foundation
import SQLite3

print("running")

let messagesDBPath = NSString(string: "~/Library/Messages/chat.db").expandingTildeInPath
var db: OpaquePointer?

// Connect to the SQLite database
if sqlite3_open(messagesDBPath, &db) != SQLITE_OK {
  print("Error opening database: \(String(cString: sqlite3_errmsg(db)))")
  exit(1)
} else {
  print("Connected to database: \(messagesDBPath)")
}

// Define a function to decode attributedBody data
func decodeAttributedBody(data: Data) -> NSAttributedString? {
  do {
    return try NSKeyedUnarchiver.unarchiveTopLevelObjectWithData(data) as? NSAttributedString
  } catch {
    print("Error decoding data: \(error)")
    return nil
  }
}

// Query the most recent 10 messages
let query = "SELECT attributedBody FROM message ORDER BY date DESC LIMIT 10"
var statement: OpaquePointer?

if sqlite3_prepare_v2(db, query, -1, &statement, nil) == SQLITE_OK {
  while sqlite3_step(statement) == SQLITE_ROW {
    let length = sqlite3_column_bytes(statement, 0)
    print(length)
    let bytes = sqlite3_column_blob(statement, 0)
    let data = Data(bytes: bytes!, count: Int(length))
    if let attributedString = decodeAttributedBody(data: data) {
      print(attributedString.string)
    } else {
      print("failed to parse")
    }
  }
} else {
  print("Error preparing statement: \(String(cString: sqlite3_errmsg(db)))")
}

sqlite3_finalize(statement)
sqlite3_close(db)
