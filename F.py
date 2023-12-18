import javafx.application.Application;
import javafx.embed.swing.SwingNode;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import org.apache.commons.math3.analysis.function.Exp;
import org.apache.commons.math3.stat.descriptive.DescriptiveStatistics;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.statistics.HistogramDataset;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.Random;

public class JavaFXApp extends Application {

    private double[] randomArray;

    public static void main(String[] args) {
        launch(args);
    }

    public void start(Stage primaryStage) {
        primaryStage.setTitle("JavaFX and JFreeChart App");

        VBox vBox = new VBox(10);

        Label label = new Label("Tensor Operations and Visualization");
        vBox.getChildren().add(label);

        Button sumButton = new Button("Calculate Sum");
        sumButton.setOnAction(e -> calculateSum());
        vBox.getChildren().add(sumButton);

        Button meanButton = new Button("Calculate Mean");
        meanButton.setOnAction(e -> calculateMean());
        vBox.getChildren().add(meanButton);

        Button visualizeButton = new Button("Visualize Tensor");
        visualizeButton.setOnAction(e -> visualizeTensor());
        vBox.getChildren().add(visualizeButton);

        SwingNode swingNode = new SwingNode();
        vBox.getChildren().add(swingNode);

        Scene scene = new Scene(vBox, 400, 300);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void calculateSum() {
        double sum = 0;
        for (double value : randomArray) {
            sum += value;
        }
        displayResult("Sum of tensor elements: " + sum);
    }

    private void calculateMean() {
        DescriptiveStatistics stats = new DescriptiveStatistics();
        for (double value : randomArray) {
            stats.addValue(value);
        }
        displayResult("Mean of tensor elements: " + stats.getMean());
    }

    private void visualizeTensor() {
        HistogramDataset dataset = new HistogramDataset();
        dataset.setType(HistogramDataset.TYPE_RELATIVE_FREQUENCY);
        dataset.addSeries("Tensor Values", randomArray, 10);

        JFreeChart chart = ChartFactory.createHistogram(
                "Distribution of Tensor Values",
                "Tensor Values",
                "Frequency",
                dataset,
                PlotOrientation.VERTICAL,
                true,
                true,
                false
        );

        XYPlot plot = (XYPlot) chart.getPlot();
        plot.setDomainPannable(true);
        plot.setRangePannable(true);

        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(300, 200));

        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Histogram");
            frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            frame.getContentPane().add(chartPanel);
            frame.pack();
            RefineryUtilities.centerFrameOnScreen(frame);
            frame.setVisible(true);
        });
    }

    private void displayResult(String result) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Result");
            frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            frame.getContentPane().add(new JLabel(result));
            frame.pack();
            RefineryUtilities.centerFrameOnScreen(frame);
            frame.setVisible(true);
        });
    }

    @Override
    public void init() {
        generateRandomArray();
    }

    private void generateRandomArray() {
        Random random = new Random();
        randomArray = new double[1000];
        for (int i = 0; i < randomArray.length; i++) {
            randomArray[i] = random.nextDouble();
        }
    }
}
