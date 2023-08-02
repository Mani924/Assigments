u_i=raw_input("Enter input to check given input is alphabates only or not")
if u_i.isalpha():
    print "input contans alphabates only"
else:
    print "input not contains all alphabates "
test_is_exempt {
  # construct some input
  input := {
    "review": {
      "object": {
        "spec": {
          "containers": [
            {
              "name": "test-container",
              "image": "test-image",
              "securityContext": {
                "runAsUser": 150,
                "runAsGroup": 150,
                "supplementalGroups": [150],
                "fsGroup": 150
              }
            }
          ]
        }
      }
    },
    "parameters": {
      "runAsUser": {
        "rule": "MustRunAs",
        "ranges": [
          {
            "min": 100,
            "max": 200
          }
        ]
      },
      "runAsGroup": {
        "rule": "MustRunAs",
        "ranges": [
          {
            "min": 100,
            "max": 200
          }
        ]
      },
      "supplementalGroups": {
        "rule": "MustRunAs",
        "ranges": [
          {
            "min": 100,
            "max": 200
          }
        ]
      },
      "fsGroup": {
        "rule": "MustRunAs",
        "ranges": [
          {
            "min": 100,
            "max": 200
          }
        ]
      }
    }
  }


runAsUserRange := {"min": 100, "max": 200}
runAsGroupRange := {"min": 100, "max": 200}
supplementalGroupsRange := {"min": 100, "max": 200}
fsGroupRange := {"min": 100, "max": 200}
  # Assume container to be exempt
  not is_exempt(input.review.object.spec.containers[0])
}
