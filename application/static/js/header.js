    function openSavedWorkout(workoutName) {
      var i;
      var x = document.getElementsByClassName("savedWorkout");
      for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
      }
      document.getElementById(workoutName).style.display = "block";
    }

    function deleteWorkout(id) {

        var input = document.createElement("input");

        input.setAttribute("type", "hidden");

        input.setAttribute("name", "delete_id");

        input.setAttribute("value", id);

        document.getElementById("delete_saved_workout").appendChild(input);
        document.getElementById('delete_saved_workout').submit();

        return
    }

    function beginWorkout(id) {

        var input = document.createElement("input");

        input.setAttribute("type", "hidden");

        input.setAttribute("name", "workout_id");

        input.setAttribute("value", id);

        document.getElementById("begin_saved_workout").appendChild(input);
        document.getElementById('begin_saved_workout').submit();

        return
    }

    function addWorkout(day_id, workout_name) {

        if (workout_name == "Rest") {
            document.getElementById(day_id).innerHTML = "Rest";
        } else {
            document.getElementById(day_id).innerHTML = workout_name;
        }

        document.getElementById("Add_Monday").style.display = "none";
        document.getElementById("Add_Tuesday").style.display = "none";
        document.getElementById("Add_Wednesday").style.display = "none";
        document.getElementById("Add_Thursday").style.display = "none";
        document.getElementById("Add_Friday").style.display = "none";
        document.getElementById("Add_Saturday").style.display = "none";
        document.getElementById("Add_Sunday").style.display = "none";

    }