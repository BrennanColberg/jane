// swift-tools-version: 5.7

import PackageDescription

let package = Package(
  name: "MySwiftProject",
  products: [
    .executable(name: "MySwiftProject", targets: ["MySwiftProject"]),
  ],
  dependencies: [
    .package(url: "https://github.com/stephencelis/SQLite.swift.git", from: "0.12.2")
  ],
  targets: [
    .executableTarget( name: "MySwiftProject",dependencies: [
      .product(name: "SQLite", package: "SQLite.swift"),
    ]),
  ]
)
