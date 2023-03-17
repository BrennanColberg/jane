// swift-tools-version: 5.7

import PackageDescription

let package = Package(
    name: "MySwiftProject",
    products: [
        .executable(name: "MySwiftProject", targets: ["MySwiftProject"]),
    ],
    dependencies: [
    ],
    targets: [
        .executableTarget( name: "MySwiftProject",dependencies: []),
    ]
)
